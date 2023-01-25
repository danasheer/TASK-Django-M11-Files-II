from django import forms
from .models import Island

class IslandForm(forms.ModelForm):
    class Meta:
        model=Island
        fields =["name"]
    