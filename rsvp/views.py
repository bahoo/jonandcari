# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from functools import wraps
from .models import Rsvp
from .forms import RsvpForm
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum


def index(request):
    key = request.session.get('key', '')
    if key:
        try:
            Rsvp.objects.get(key=key)
            return HttpResponseRedirect(reverse('rsvp'))
        except:
            pass

    # if we're still here then the above didn't bomb and the key is legit.
    return render(request, 'index.html')


def save_the_date(request):
    return render(request, 'savethedate.html')


def no_route(request):
    render(request, 'rsvp_noroute.html')


def valid_rsvp_required(method):
    @wraps(method)
    def wrapper(request, *args, **kwargs):
        # maybe we already have this shit.
        if not hasattr(request, 'rsvp'):
            # first peep the session.
            key = request.session.get('key', '')
            if not key:
                # dude we can't help you.
                return HttpResponseRedirect(reverse('index'))
            try:
                rsvp = Rsvp.objects.get(key=key)
            except:
                return HttpResponseRedirect(reverse('no_route'))
            # if we're still here then the above didn't bomb and the key is legit.
            request.rsvp = rsvp
            return method(request, *args, **kwargs)
    return wrapper


def secret_handshake(request, key, destination=None):
    if destination == 'secrethandshake':
        destination = 'rsvp'
    try:
        Rsvp.objects.get(key=key)
    except:
        return HttpResponseRedirect(reverse('no_route'))
    # if we're still here, then the key is valid.
    request.session['key'] = key
    return HttpResponseRedirect(reverse(destination or 'index'))


@valid_rsvp_required
def rsvp(request):
    rsvp = request.rsvp
    rsvp_form = RsvpForm(request.POST or None, instance=rsvp)
    submitted = False
    if request.POST:
        submitted = True
        if rsvp_form.is_valid():
            rsvp_form.save()
        else:
            print rsvp_form.errors
    already_rsvped = (rsvp.is_attending is not None)
    return render(request, 'rsvp.html', {'rsvp': rsvp, 'rsvp_form': rsvp_form, 'submitted': submitted, 'already_rsvped': already_rsvped})


@valid_rsvp_required
def template(request, destination):
    return render(request, '%s.html' % destination, {'rsvp': request.rsvp, 'texty': True})


@staff_member_required
def count(request):
    everyone = Rsvp.objects.all()
    reporting = everyone.exclude(is_attending=None)
    attendees = everyone.filter(is_attending=True)
    not_attending = everyone.filter(is_attending=False)
    possible = everyone.exclude(is_attending=False)
    count = attendees.aggregate(Sum('count'))['count__sum']
    maximum = possible.aggregate(Sum('count'))['count__sum']
    pct_reporting = "{0:.0f}%".format(100 * float(reporting.count()) / float(everyone.count()))
    return render(request, 'count.html', {'count': count, 'attendees': attendees, 'pct_reporting': pct_reporting, 'not_attending': not_attending, 'maximum': maximum})
