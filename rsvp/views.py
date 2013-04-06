# Create your views here.
from django.shortcuts import render
from .models import Rsvp
from .forms import RsvpForm


def index(request):
    return render(request, 'index.html')


def save_the_date(request):
    return render(request, 'savethedate.html')


def rsvp(request, key):
    rsvp = Rsvp.objects.get(key=key)
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
