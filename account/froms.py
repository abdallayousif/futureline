from django import forms
from django.db.models import fields
from . models import Invitation, UserBase



class RegistrtaionForm(forms.ModelForm):
    user_name = forms.CharField(label='ادخل اسم المستخدم', max_length=50 , min_length=4 ,help_text='Required')
    email =  forms.EmailField(label='ادخل الايميل', max_length=100, help_text='Required', error_messages={'required': 'sorry you need an email'})
    password =  forms.CharField(label='كلمه السر', widget=forms.PasswordInput)
    password2 =  forms.CharField(label='اعد كلمة السر', widget=forms.PasswordInput)
    first_name = forms.CharField(label='ادخل اسم بالكامل', max_length=50 , min_length=4 ,help_text='Required')
    phone_number = forms.IntegerField(label='رقم الهاتف',help_text='Required')


    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError('اسم المستخدم موجود ')
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('كلمة السر غير مطابقه')
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError('من فضلك استخدم ايميل اخر')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': ' اسم المستخدم يجب ان يكون بالانجليزيه'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'ايميل ', 'name':'email'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'كلمة السر '}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': ' اعد كلمة السر '}
        )
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'الاسم بالكامل'}
        )
        self.fields['phone_number'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'رقم الهاتف  '}
        )

class UserEditForm(forms.ModelForm):
     
    
    create = forms.ModelChoiceField(queryset=UserBase.objects.all(),
            label='الرقم التعريفي',  widget=forms.Select(
            attrs={'class': 'form-control mb-3', 'id': 'form-email'}))


    full_name = forms.CharField(
        label='اسمك الاول', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'اسمك الاول', 'id': 'form-lastname'}))

    phone_number = forms.CharField(label='رقم الهاتف', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'رقم الهاتف', 'id': 'form-phone'}))

    class Meta:
        model = Invitation
        fields = ('create','full_name')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].required = True
        
