from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email"]
		
class RegForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()