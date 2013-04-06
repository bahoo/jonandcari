# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rsvp.message'
        db.add_column(u'rsvp_rsvp', 'message',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rsvp.message'
        db.delete_column(u'rsvp_rsvp', 'message')


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
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True'})
        }
    }

    complete_apps = ['rsvp']