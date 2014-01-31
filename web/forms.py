from django import forms
from models import Alumni, Moseyer

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni

class MoseyerForm(forms.ModelForm):
    class Meta:
        model = Moseyer