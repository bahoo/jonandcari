from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'rsvp.views.index', name='index'),
    url(r'^savethedate\.html$', 'rsvp.views.save_the_date', name='save_the_date'),
    url(r'^(?P<destination>(about-us|getting\-here|wedding\-party|gifts|rsvp|secrethandshake))(?:\/)(?P<key>\w+)$', 'rsvp.views.secret_handshake', name='secret_handshake'),
    url(r'^(?P<destination>(about-us|getting\-here|wedding\-party|gifts))$', 'rsvp.views.template', name='template'),
    url(r'^rsvp$', 'rsvp.views.rsvp', name='rsvp'),

    url(r'^lost$', 'rsvp.views.no_route', name='no_route'),
    url(r'^admin/', include(admin.site.urls)),
)
