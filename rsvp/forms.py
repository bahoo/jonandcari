from django import forms
from .models import Rsvp


class RsvpForm(forms.ModelForm):
    class Meta:
        model = Rsvp
        fields = ['is_attending', 'message', 'count', 'location', 'attendees']
        widgets = {'is_attending': forms.HiddenInput, 'location': forms.HiddenInput, 'count': forms.TextInput(attrs={'class': 'count', 'maxlength': '2'})}
