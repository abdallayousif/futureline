
from urllib import request

from django.shortcuts import redirect, render

from .froms import RegistrtaionForm, UserEditForm
from .models import Invitation, UserBase


# Create your views here.
def home(request):
    invite = Invitation.objects.all()
    return render(request, 'home.html', {'invite':invite})




def SinUp(request):
    if request.method == 'POST':
        registerfrom = RegistrtaionForm(request.POST)
        if registerfrom.is_valid():
            user = registerfrom.save(commit=False)
            user.email = registerfrom.cleaned_data['email']
            print(registerfrom.cleaned_data['email'])
            user.set_password(registerfrom.cleaned_data['password'])
            user.full_name = registerfrom.cleaned_data['first_name']
            user.phone = str(registerfrom.cleaned_data['phone_number'])
            user.is_active = True
            user.save()
            return redirect('account:Counter')
    else:
        registerfrom = RegistrtaionForm()
    
    return render(request, 'register.html', {'form': registerfrom})

def Invition(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, request.FILES)
        
        if user_form.is_valid():
            user_form.save()
        else:
            print(user_form.errors)
        return redirect('account:Counter')
    return render(request, 'addPerson.html', {'user_form': UserEditForm})
