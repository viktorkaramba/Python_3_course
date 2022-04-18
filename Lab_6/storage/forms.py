from django import forms
from django.forms import ModelForm, NumberInput

from .models import Number


class UserForm(ModelForm):
    class Meta:
        model = Number
        fields = ['id_se']
        widgets = {
            'id_se': NumberInput(attrs={
                'placeholder': 'ID of section'
            })
        }

