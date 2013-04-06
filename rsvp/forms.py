from django import forms
from .models import Rsvp


class RsvpForm(forms.ModelForm):
    class Meta:
        model = Rsvp
        fields = ['is_attending', 'message', 'count', 'location']
        widgets = {'is_attending': forms.HiddenInput}
