from django import forms
from .models import Terreno

class TerrenoForm(forms.ModelForm):
    class Meta:
        model = Terreno
        fields = '__all__'

