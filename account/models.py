import email
from tabnanny import verbose
from unicodedata import name
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _




class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to in staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to in is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('يجب ان تدخل الايميل'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)

        user.set_password(password)
        user.save()
        return user

class UserBase(AbstractBaseUser,PermissionsMixin):
    email =     models.EmailField(_('email_address'), unique=True) 
    user_name = models.CharField(max_length=150 , unique=True)
    full_name = models.CharField(max_length=150, blank=True)
    phone =     models.CharField(max_length=150, default='125469032')
    inveate =   models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff =  models.BooleanField(default=False)
    created =   models.DateTimeField(auto_now_add=True)

    objects = CustomAccountManager()

    
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'
    
    def __str__(self):
        return self.inveate

    def save(self, *args, **kwargs):
        self.inveate = (self.user_name[:2]).upper() + self.phone[-4:]
        super().save(*args, **kwargs)

class Invitation(models.Model):
    create = models.ForeignKey(UserBase , on_delete=models.RESTRICT)
    full_name = models.CharField(max_length=150)
    phone = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'Invitation'
        verbose_name_plural = 'Invitation'
    
    def __str__(self):
        return self.full_name