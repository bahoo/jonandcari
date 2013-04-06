# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Attendee', fields ['is_primary', 'rsvp']
        db.delete_unique(u'rsvp_attendee', ['is_primary', 'rsvp_id'])

        # Deleting model 'Attendee'
        db.delete_table(u'rsvp_attendee')

        # Adding field 'Rsvp.name'
        db.add_column(u'rsvp_rsvp', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Rsvp.email'
        db.add_column(u'rsvp_rsvp', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', unique=True, max_length=75),
                      keep_default=False)


        # Changing field 'Rsvp.is_attending'
        db.alter_column(u'rsvp_rsvp', 'is_attending', self.gf('django.db.models.fields.NullBooleanField')(null=True))

    def backwards(self, orm):
        # Adding model 'Attendee'
        db.create_table(u'rsvp_attendee', (
            ('phone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_over_21', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('rsvp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Rsvp'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'rsvp', ['Attendee'])

        # Adding unique constraint on 'Attendee', fields ['is_primary', 'rsvp']
        db.create_unique(u'rsvp_attendee', ['is_primary', 'rsvp_id'])

        # Deleting field 'Rsvp.name'
        db.delete_column(u'rsvp_rsvp', 'name')

        # Deleting field 'Rsvp.email'
        db.delete_column(u'rsvp_rsvp', 'email')


        # Changing field 'Rsvp.is_attending'
        db.alter_column(u'rsvp_rsvp', 'is_attending', self.gf('django.db.models.fields.BooleanField')())

    models = {
        u'rsvp.rsvp': {
            'Meta': {'object_name': 'Rsvp'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_attending': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['rsvp']