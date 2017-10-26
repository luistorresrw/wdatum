#-*-coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Nacionalidad(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class NivelInstruccion(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class RegimenTenencia(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class AnioConstruccion(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class MaterialEstructura(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class TipoProduccion(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class EleccionCultivo(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class TipoCultivo(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class Especie(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class FactorClimatico(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class TripleLavado(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion


class Asesoramiento(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion

# ---------------------------------------------------------


class Establecimiento(models.Model):
	nombre = models.CharField(max_length=45)
	numero = models.CharField(max_length=45)
	posLatitud = models.CharField(max_length=45)
	posLongitud = models.CharField(max_length=45)

	def __unicode__(self):
		return self.nombre
