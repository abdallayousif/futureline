from unicodedata import name
from django.urls import include, path
from .  import views

app_name= "account"

urlpatterns = [
    path("" , views.home , name="Counter"), 
    path("regstier/", views.SinUp , name='SinUp'),
    path("invite/", views.Invition , name='Invition'),
]
