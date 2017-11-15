#-*-coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField

class Usuario(User):
	ROL_CHOICES = (
        ('Administrador', 'Administrador'),
        ('Operador', 'Operador'),
        ('Encuestador', 'Encuestador'),
    )
	dni = models.CharField(max_length=8)
	rol = models.CharField(max_length=15, choices=ROL_CHOICES)

class Nacionalidad(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class NivelInstruccion(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class RegimenTenencia(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class AnioConstruccion(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class MaterialEstructura(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class TipoProduccion(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class EleccionCultivo(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class TipoCultivo(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class Especie(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class FactorClimatico(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class TripleLavado(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class Asesoramiento(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

class Establecimiento(models.Model):
	nombre = models.CharField(max_length=45)
	numero = models.CharField(max_length=45)
	posLatitud = models.FloatField()
	posLongitud = models.FloatField()
	#foto = models.ImageField(upload_to='fotos/', null=True)

	def __str__(self):
		return u'%s' % self.nombre
