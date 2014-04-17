# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import PersonalData


class PersonalDataForm(ModelForm):
    class Meta:
        model = PersonalData


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")