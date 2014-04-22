# coding=utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.staticfiles.storage import staticfiles_storage
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from accounts.models import PersonalData


class CalendarWidget(forms.DateInput):
    def prop_media(self):
        return forms.Media(css={'all': (staticfiles_storage.url('css/jquery-ui-1.10.4.custom.css'),)},
                           js=(
                               staticfiles_storage.url('js/jquery-1.10.2.js'),
                               staticfiles_storage.url('js/jquery.form.js'),
                               staticfiles_storage.url('js/jquery-ui-1.10.4.custom.js'),
                               staticfiles_storage.url('js/calendar.js')))

    media = property(prop_media)

    def __init__(self, params='', attrs=None):
        self.params = params
        super(CalendarWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(CalendarWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
                $(document).ready(function () {
                    $("#id_%s").datepicker({%s});
                })
                    </script>''' % (name, self.params,))


class PersonalDataForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonalDataForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget = CalendarWidget(
            params="minDate: -36500, maxDate: 0, dateFormat: 'yy-mm-dd', showButtonPanel: true",
            attrs={'class': 'datepicker'}
        )

    class Meta:
        model = PersonalData
        fields = ("name", "surname", "date_of_birth", "bio", "email", "jabber", "skype", "other_contact", "userpic")
        widgets = {"bio": forms.Textarea(attrs={'rows': 4, 'cols': 50}),
                   "other_contact": forms.Textarea(attrs={'rows': 4, 'cols': 50})}


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")