from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

BOOLEAN_CHOICES = ((True, 'Yes'), (False, 'No'))

# Create your models here.
class Rsvp(models.Model):
    is_attending = models.BooleanField(default=True, choices=BOOLEAN_CHOICES)
    location = models.CharField(max_length=255)
    key = models.CharField(max_length=32, unique=True)


class Attendee(models.Model):
    rsvp = models.ForeignKey(Rsvp)
    name = models.CharField(max_length=255)
    is_over_21 = models.BooleanField(default=True)
    is_primary = models.BooleanField(default=False)
    phone = PhoneNumberField()
    email = models.EmailField()

    class Meta:
        unique_together = (('is_primary', 'rsvp'),)
