# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Request_data'
        db.create_table(u'accounts_request_data', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('method_request', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('time_request', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'accounts', ['Request_data'])


    def backwards(self, orm):
        # Deleting model 'Request_data'
        db.delete_table(u'accounts_request_data')


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
        },
        u'accounts.request_data': {
            'Meta': {'object_name': 'Request_data'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method_request': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'time_request': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['accounts']