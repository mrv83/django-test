# coding=utf-8
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.contrib.sites.models import Site
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from south.models import MigrationHistory


PRIORITY_CHOICES = (
    ('0', '0'),
    ('1', '1'),
)


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

    def __unicode__(self):
        return self.name


class RequestData(models.Model):
    path = models.CharField(max_length=256)
    method_request = models.CharField(max_length=16)
    time_request = models.DateField(auto_now_add=True)
    priority = models.CharField(max_length=128, blank=True, default='0', choices=PRIORITY_CHOICES)

    def __unicode__(self):
        return self.path


class DBAction(models.Model):
    action_name = models.CharField(max_length=32, default='', blank=True, null=True)
    action_time = models.DateTimeField(auto_now_add=True)
    action_model_name = models.CharField(max_length=32, default='', blank=True, null=True)
    action_model_id = models.IntegerField(blank=True, null=True)


EXCLUDE_TABLE = [DBAction, ContentType, Session, Site, MigrationHistory]


@receiver(post_save)
def db_action_save(sender, **kwargs):
    if sender not in EXCLUDE_TABLE:
        if not kwargs["raw"]:
            act = DBAction()
            db_record = kwargs["instance"]
            act.action_model_id = db_record.id
            act.action_model_name = db_record._meta.module_name
            if kwargs["created"]:
                act.action_name = "created"
            else:
                act.action_name = "edited"
            act.save()


@receiver(post_delete)
def db_action_delete(sender, **kwargs):
    if sender not in EXCLUDE_TABLE:
        act = DBAction()
        db_record = kwargs["instance"]
        act.action_model_id = db_record.id
        act.action_model_name = db_record._meta.module_name
        act.action_name = "deleted"
        act.save()
