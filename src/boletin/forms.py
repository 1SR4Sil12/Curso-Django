from django import forms
from .models import Registrado

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	edad = forms.IntegerField()