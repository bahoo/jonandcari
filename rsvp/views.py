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
    rsvp_form = RsvpForm()
    return render(request, 'rsvp.html', {'rsvp': rsvp, 'rsvp_form': rsvp_form})
