# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rsvp'
        db.create_table(u'rsvp_rsvp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_attending', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal(u'rsvp', ['Rsvp'])

        # Adding model 'Attendee'
        db.create_table(u'rsvp_attendee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rsvp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Rsvp'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_over_21', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'rsvp', ['Attendee'])

        # Adding unique constraint on 'Attendee', fields ['is_primary', 'rsvp']
        db.create_unique(u'rsvp_attendee', ['is_primary', 'rsvp_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Attendee', fields ['is_primary', 'rsvp']
        db.delete_unique(u'rsvp_attendee', ['is_primary', 'rsvp_id'])

        # Deleting model 'Rsvp'
        db.delete_table(u'rsvp_rsvp')

        # Deleting model 'Attendee'
        db.delete_table(u'rsvp_attendee')


    models = {
        u'rsvp.attendee': {
            'Meta': {'unique_together': "(('is_primary', 'rsvp'),)", 'object_name': 'Attendee'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_over_21': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'rsvp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Rsvp']"})
        },
        u'rsvp.rsvp': {
            'Meta': {'object_name': 'Rsvp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_attending': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['rsvp']