# coding=utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from accounts.models import PersonalData


class CalendarWidget(forms.TextInput):

    def _media(self):
        return forms.Media(css={'all': ('/static/css/jquery-ui-1.10.4.custom.css',)},
                           js=('/static/js/jquery-1.10.2.js', '/static/js/jquery.form.js',
                                 '/static/js/jquery-ui-1.10.4.custom.js', '/static/js/calendar.js'))
    media = property(_media)


class PersonalDataForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PersonalDataForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget = CalendarWidget(attrs=None)

    class Meta:
        model = PersonalData
        fields = ("name", "surname", "date_of_birth", "bio", "email", "jabber", "skype", "other_contact", "userpic")
        widgets = {"bio": forms.Textarea(attrs={'rows': 4, 'cols': 50}),
                   "other_contact": forms.Textarea(attrs={'rows': 4, 'cols': 50})}



class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")