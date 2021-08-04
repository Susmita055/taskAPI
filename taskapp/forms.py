from typing import Text
from django import forms
from django.db import models
from django.db.models import fields
from .models import Register
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
        class Meta:
            model=Register
            fields=("Email", "Password","FirstName", "LastName")
        

