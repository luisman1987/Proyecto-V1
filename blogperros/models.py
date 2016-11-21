from django.db import models
from django.contrib import admin

class Perro(models.Model):
    nombre = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    imagen = models.FileField(null=True,blank=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre

class Persona(models.Model):
    dpi = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    foto = models.FileField(null=True,blank=True)
    perros = models.ManyToManyField(Perro,through ='Asignacion')
    def __str__(self):              # __unicode__ on Python 2
        return self.dpi


class Asignacion(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class PerroAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class PersonaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)
