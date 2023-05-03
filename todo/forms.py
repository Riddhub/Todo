from django import forms
from .models import *


class AddNoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter todo e.g. Delete junk files",
                "aria - label": "Todo",
                "aria - describedby": "add-btn",
        }),
        }



