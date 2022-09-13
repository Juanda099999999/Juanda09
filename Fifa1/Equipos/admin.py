from django.contrib import admin
from .models import *

admin.site.register(Posicion)

admin.site.register(Rol)

admin.site.register(Nacionalidad)

@admin.register(Equipo)

class EquipoAdmin(admin.ModelAdmin):
    list_display = ("Imagen_escudo","Imagen_bandera","Nombre")

@admin.register(Jugador)

class Jugador(admin.ModelAdmin):
    list_display = ("Imagen_escudo","Imagen_bandera","Foto_jugador","Nombre","Edad","equipo","Posicion","Numero","titular")
    list_filter = ("equipo","Posicion")
    search_fields = ["Nombre"]





@admin.register(Tecnico)

class Tecnico(admin.ModelAdmin):
    list_display = ("Foto_tecnico","Imagen_bandera","Imagen_escudo","Nombre","Edad","Nacionalidad","Rol")