from django import forms
from .models import Study_list

class Study_form(forms.ModelForm):

    class Meta:
        model = Study_list
        fields = ('name', 'intro',)