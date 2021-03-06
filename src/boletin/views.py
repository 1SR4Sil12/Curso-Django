from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrado

def inicio(request):
	titulo = "Bienvenidos"
	if request.user.is_authenticated():
		titulo = "Bienvenid@ %s" %(request.user)
	form = RegModelForm(request.POST or None)
	context = {
		"titulo": titulo,
		"el_form": form,
		}
	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = "PERSONA ANONIMA"
		instance.save()

		context = {
			"titulo": "Gracias %s!" %(nombre)
			}

		if not nombre:
			context ={
				"titulo": "Gracias %s!" %(email)

			}
		print instance
		print instance.timestamp
	#	form_data = form.cleaned_data
	#	abc = form_data.get("email")
	#	abc2 = form_data.get("nombre")
	#	obj = Registrado.objects.create(email=abc, nombre=abc2)
	
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = Registrado.objects.all().order_by("-timestamp")#.filter(nombre__icontains="a")
		context ={
			"queryset": queryset,
		}
	return render(request, "inicio.html", context)
# Create your views here.
def contact(request):
	titulo = "Contactanos"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = "Form de Contacto"
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "otroemail@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email )
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)
		#print email, mensaje, nombre
	context = {
		"form": form,
		"titulo": titulo,
	}
	return render (request, "forms.html", context)