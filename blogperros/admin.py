from django.contrib import admin
from blogperros.models import Perro,Persona,Asignacion,PerroAdmin,PersonaAdmin

admin.site.register(Perro, PerroAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Asignacion)
