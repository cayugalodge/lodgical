# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsArticle'
        db.create_table(u'web_newsarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=1024)),
        ))
        db.send_create_signal(u'web', ['NewsArticle'])

        # Adding model 'About'
        db.create_table(u'web_about', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=2044)),
        ))
        db.send_create_signal(u'web', ['About'])

        # Adding model 'Alumni'
        db.create_table(u'web_alumni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'web', ['Alumni'])

        # Adding model 'Contact'
        db.create_table(u'web_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'web', ['Contact'])

        # Adding model 'Moseyer'
        db.create_table(u'web_moseyer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'web', ['Moseyer'])

        # Adding model 'MoseyEvent'
        db.create_table(u'web_moseyevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2048)),
        ))
        db.send_create_signal(u'web', ['MoseyEvent'])


    def backwards(self, orm):
        # Deleting model 'NewsArticle'
        db.delete_table(u'web_newsarticle')

        # Deleting model 'About'
        db.delete_table(u'web_about')

        # Deleting model 'Alumni'
        db.delete_table(u'web_alumni')

        # Deleting model 'Contact'
        db.delete_table(u'web_contact')

        # Deleting model 'Moseyer'
        db.delete_table(u'web_moseyer')

        # Deleting model 'MoseyEvent'
        db.delete_table(u'web_moseyevent')


    models = {
        u'web.about': {
            'Meta': {'object_name': 'About'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '2044'})
        },
        u'web.alumni': {
            'Meta': {'object_name': 'Alumni'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'web.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'web.moseyer': {
            'Meta': {'object_name': 'Moseyer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'web.moseyevent': {
            'Meta': {'object_name': 'MoseyEvent'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2048'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'web.newsarticle': {
            'Meta': {'object_name': 'NewsArticle'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['web']