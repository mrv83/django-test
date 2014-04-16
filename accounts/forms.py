# coding=utf-8
from django.forms import ModelForm
from accounts.models import PersonalData


class PersonalDataForm(ModelForm):
    class Meta:
        model = PersonalData
