from django.contrib import admin

from account.models import Invitation, UserBase

# Register your models here.


admin.site.register(UserBase)
admin.site.register(Invitation)