# coding=utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from accounts.models import PersonalData


class PersonalDataForm(ModelForm):
    class Meta:
        model = PersonalData
        fields = ("name", "surname", "date_of_birth", "bio", "email", "jabber", "skype", "other_contact", "userpic")
        widgets = {"bio": forms.Textarea(attrs={'rows': 4, 'cols': 50}),
                   "other_contact": forms.Textarea(attrs={'rows': 4, 'cols': 50})}


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")