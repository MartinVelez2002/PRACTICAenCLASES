from django.contrib import admin

# Register your models here.
from aplicaciones.core.models import *
admin.site.register(Linea)
admin.site.register(Grupo)