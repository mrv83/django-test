# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DBAction'
        db.create_table(u'accounts_dbaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_name', self.gf('django.db.models.fields.CharField')(default='', max_length=32, null=True, blank=True)),
            ('action_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('action_model_name', self.gf('django.db.models.fields.CharField')(default='', max_length=32, null=True, blank=True)),
            ('action_model_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'accounts', ['DBAction'])


    def backwards(self, orm):
        # Deleting model 'DBAction'
        db.delete_table(u'accounts_dbaction')


    models = {
        u'accounts.dbaction': {
            'Meta': {'object_name': 'DBAction'},
            'action_model_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'action_model_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'action_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'accounts.personaldata': {
            'Meta': {'object_name': 'PersonalData'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'other_contact': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'userpic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'accounts.requestdata': {
            'Meta': {'object_name': 'RequestData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method_request': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'time_request': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['accounts']