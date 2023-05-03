from django import forms
from .models import *


class AddNoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = '__all__'


