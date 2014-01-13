from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from customer.models import Customer
from core.models import Vendor, Product



#for registration
class Profile(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('name', 'password', 'last_name', 'first_name', 'last_login', 'groups', 'user_permissions' )



class Dashboard(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = ('user')





class Addproduct(forms.ModelForm):
    class Meta:
        model = Product




