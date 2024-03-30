from django import forms
from .models import ImportantClient

class ImportantClientForm(forms.ModelForm):
    class Meta:
        model = ImportantClient
        fields = ['name', 'address', 'image']
