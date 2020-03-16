from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

# from .models import User, AgencyAdmin

# class AgencyAdminForm(UserCreationForm):
#     name = forms.TimeField()
#     email = 


class alertletterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')