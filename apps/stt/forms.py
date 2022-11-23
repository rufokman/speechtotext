from .models import *
from django import forms

class RecorderForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ('dtcreate', 'language', 'audio_name' )