from django.core import mail
from django.template.loader import render_to_string
from rsvp.models import Rsvp

connection = mail.get_connection()
connection.open()

for r in Rsvp.objects.all():
    message = render_to_string('email.txt', {'rsvp': r})
    email = mail.EmailMessage('RSVP Time Suckas', message, 'jon.plus.cari@gmail.com',
                          [r.email], connection=connection)
    email.send()
    email = None

connection.close()