from django.db import models


class PersonalData(models.Model):
    name = models.CharField(max_length=32, default='')
    surname = models.CharField(max_length=32, default='')
    date_of_birth = models.DateField(blank=True)
    bio = models.TextField(max_length=1024, blank=True, default='')
    email = models.EmailField(blank=True)
    jabber = models.EmailField()
    skype = models.CharField(max_length=32, blank=True, default='')
    other_contact = models.TextField(max_length=1024, blank=True, default='')
    userpic = models.ImageField(upload_to='avatar', blank=True, null=True)


class RequestData(models.Model):
    path = models.CharField(max_length=256)
    method_request = models.CharField(max_length=16)
    time_request = models.DateField(auto_now_add=True)
