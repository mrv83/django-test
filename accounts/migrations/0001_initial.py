# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Personal_data'
        db.create_table(u'accounts_personal_data', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('surname', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(default='', max_length=1024, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('other_contact', self.gf('django.db.models.fields.TextField')(default='', max_length=1024, blank=True)),
        ))
        db.send_create_signal(u'accounts', ['Personal_data'])


    def backwards(self, orm):
        # Deleting model 'Personal_data'
        db.delete_table(u'accounts_personal_data')


    models = {
        u'accounts.personal_data': {
            'Meta': {'object_name': 'Personal_data'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'other_contact': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'})
        }
    }

    complete_apps = ['accounts']