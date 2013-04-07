from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'rsvp.views.index', name='index'),
    url(r'^savethedate\.html$', 'rsvp.views.save_the_date', name='save_the_date'),
    url(r'^rsvp/(?P<key>\w+)$', 'rsvp.views.rsvp', name='rsvp'),
    url(r'^rsvp/$', 'rsvp.views.rsvp', name='rsvp_noroute', kwargs={'key': None}),
    url(r'^admin/', include(admin.site.urls)),
)
