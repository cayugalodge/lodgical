from django import forms
from models import Alumni, Moseyer, MoseyerComment

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni

class MoseyerForm(forms.ModelForm):
    class Meta:
        model = Moseyer
        exclude = ["application"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = MoseyerComment
        exclude = ["author", "moseyer"]