from django.contrib import admin
from .forms import RegModelForm
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["email", "nombre", "timestamp"]
	form = RegModelForm
	#list_display_links = ["nombre"]
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	search_fields = ["enamil", "nombre"]





admin.site.register(Registrado, AdminRegistrado)