from django import forms
from .models import Registrado

class RegForm(forms.Form):
	nombre = forms.CharField(required=False)
	edad = forms.IntegerField()