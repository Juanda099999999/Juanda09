from datetime import date
from distutils.command.upload import upload
from tkinter import CASCADE
from urllib.request import CacheFTPHandler
from django.db import models
from django.utils.html import format_html

class Rol(models.Model):
  Nombre = models.CharField('Rol',max_length=30)

  def __str__(self):
   return self.Nombre
    
  class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        db_table = "Rol"
        ordering = ["id"]

class Nacionalidad(models.Model):
  Nombre = models.CharField('Nacionalidad',max_length=30)

  def __str__(self):
   return self.Nombre
    
  class Meta:
        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidades"
        db_table = "Nacionalidad"
        ordering = ["id"]


class Posicion(models.Model):
    Nombre = models.CharField('Posicion',max_length=30)

    def __str__(self):
     return self.Nombre
    
    class Meta:
        verbose_name = "Posicion"
        verbose_name_plural = "Posiciones"
        db_table = "Posicion"
        ordering = ["id"]
 

class Equipo(models.Model):
    Nombre = models.CharField('Nombre del equipo',max_length= 100)
    bandera = models.ImageField('Bandera del equipo', upload_to='media')
    escudo = models.ImageField('Escudo del equipo', upload_to='media')

    def __str__(self):
     return self.Nombre
    
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = "Equipo"
        ordering = ["id"]

    def Imagen_escudo(self):
      return format_html ( '<img src= {} width="130" height="100" />', self.escudo.url )
    
    def Imagen_bandera(self):
      return format_html ( '<img src= {} width="130" height="100" />', self.bandera.url )

class Jugador(models.Model):
    foto = models.ImageField('Foto del jugador', upload_to='media')
    Nombre = models.CharField('Nombre del jugador', max_length=30)
    Posicion = models.ForeignKey(Posicion,on_delete=models.CASCADE)
    Dia_de_nacimiento = models.DateField("Dia de nacimiento")
    Edad = models.PositiveIntegerField("Edad",blank=True,null=True)
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    Numero = models.PositiveIntegerField("Numero de camiseta")
    titular = models.BooleanField("Titular",default=True)
    def Imagen_escudo(self):
      return format_html ( '<img src= {} width="130" height="100" />', self.equipo.escudo.url )
    
    def Imagen_bandera(self):
      return format_html ( '<img src= {} width="130" height="100" />', self.equipo.bandera.url )
    
    def Foto_jugador(self):
      return format_html ( '<img src= {} width="130" height="100" />', self.foto.url )
    
    @property

    def calculate_age(self):
      if(self.Dia_de_nacimiento!= None):
        Edad= date.today().year- self.Dia_de_nacimiento.year
        return Edad
    

    def save(self, *args, **kwargs):

        self.Edad = self.calculate_age

        super(Jugador, self).save(*args, **kwargs)
 
    
    def __str__(self):
     return self.Nombre
    
    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        db_table = "Jugador"
        ordering = ["id"]

class Tecnico(models.Model):
    foto = models.ImageField('Foto del tecnico', upload_to='media')
    Nombre = models.CharField('Nombre del tecnico', max_length=30)
    Dia_de_nacimiento = models.DateField("Dia de nacimiento")
    Edad = models.PositiveIntegerField("Edad",blank=True,null=True)
    Nacionalidad = models.ForeignKey(Nacionalidad,on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    Rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    def Imagen_escudo(self):
      return format_html ( '<img src= {} width="130" height="100" />', self.equipo.escudo.url )
    
    def Imagen_bandera(self):
      return format_html ( '<img src= {} width="130" height="100" />', self.equipo.bandera.url )
    
    def Foto_tecnico(self):
      return format_html ( '<img src= {} width="130" height="100" />', self.foto.url )

    
        
    @property

    def calculate_age(self):
      if(self.Dia_de_nacimiento!= None):
        Edad= date.today().year- self.Dia_de_nacimiento.year
        return Edad
    

    def save(self, *args, **kwargs):

        self.Edad = self.calculate_age

        super(Tecnico, self).save(*args, **kwargs)
 
    
    def __str__(self):
     return self.Nombre
    
    class Meta:
        verbose_name = "Tecnico"
        verbose_name_plural = "Tecnicos"
        db_table = ""
        ordering = ["id"]
    




    




 

