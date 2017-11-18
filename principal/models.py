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

	class Meta:
		db_table = 'nacionalidad'

class NivelInstruccion(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'nivel_instrucion'

class RegimenTenencia(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'regimen_tenencia'

class AnioConstruccion(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'anio_construccion'

class MaterialEstructura(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'material_construccion'

class TipoProduccion(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'tipo_produccion'

class EleccionCultivo(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'eleccion_cultivo'

class TipoCultivo(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'tipo_cultivo'

class Especie(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'especie'

class FactorClimatico(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'factor_climatico'

class TripleLavado(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'triple_lavado'

class Asesoramiento(models.Model):
	descripcion = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.descripcion

	class Meta:
		db_table = 'asesoramiento'

class Establecimiento(models.Model):
	nombre 				= models.CharField(max_length=45)
	numero 				= models.CharField(max_length=45)
	posLatitud 			= models.FloatField()
	posLongitud 		= models.FloatField()
	foto 				= models.ImageField(upload_to='fotos/', null=True)
	regimenTenencia 	= models.ForeignKey('RegimenTenencia')
	regimenOtros 		= models.CharField(max_length=50,blank=True)
	creado				= models.DateField(default=None)
	modificado 			= models.DateField(default=None)
	eliminado 			= models.DateField(default=None)

	def __str__(self):
		return u'%s' % self.nombre

	class Meta:
		db_table = 'establecimiento'

class Encuestado(models.Model):
	nombre 				= models.CharField(max_length=50)
	apellido 			= models.CharField(max_length=50)
	edad 				= models.IntegerField()
	nacionalidad 		= models.ForeignKey('Nacionalidad')
	nivelInstruccion 	= models.ForeignKey('NivelInstruccion')
	nivelCompleto 		= models.BooleanField(default=False)
	viveEstablecimiento = models.BooleanField(default=False)
	creado				= models.DateField(default=None)
	modificado 			= models.DateField(default=None)
	eliminado 			= models.DateField(default=None)

	class Meta:
		db_table = 'encuestado'

class Familia(models.Model):
	esCasado 	= models.BooleanField()
	tieneHijos 	= models.BooleanField()
	cantVarones = models.IntegerField()
	cantMujeres = models.IntegerField()
	creado		= models.DateField(default=None)
	modificado	= models.DateField(default=None)
	eliminado 	= models.DateField(default=None)

	class Meta:
		db_table = 'familia'

class Agroquimico(models.Model):
	usa 				= models.BooleanField(default=False)
	factorClimatico 	= models.ForeignKey('FactorClimatico')
	tripleLavado 		= models.ForeignKey('TripleLavado')
	asesoramiento 		= models.ForeignKey('Asesoramiento')
	asesoramientoOtro 	= models.CharField(max_length=50)
	creado				= models.DateField(default=None)
	modificado 			= models.DateField(default=None)
	eliminado 			= models.DateField(default=None)

	class Meta:
		db_table = 'agroquimico'


class Encuesta(models.Model):
	fecha = models.DateField(auto_now=True)
	establecimiento = models.ForeignKey('Establecimiento')
	encuestado = models.ForeignKey('Encuestado')
	familia = models.ForeignKey('Familia')
	agroquimico = models.ForeignKey('Agroquimico')
	creado = models.DateField(default=None)
	modificado = models.DateField(default=None)
	eliminado = models.DateField(default=None)

	class Meta:
		db_table = 'encuesta'

class Invernaculo(models.Model):
	encuesta 			= models.ForeignKey('Encuesta')
	cantidadModulos 	= models.IntegerField()
	superficieUnitaria 	= models.IntegerField()
	materialEstructura 	= models.ForeignKey('MaterialEstructura')
	anioContruccion	 	= models.ForeignKey('AnioConstruccion')
	creado				= models.DateField(default=None)
	modificado 			= models.DateField(default=None)
	eliminado 			= models.DateField(default=None)

	class Meta:
		db_table = 'invernaculo'

class Cultivo(models.Model):
	encuesta 		= models.ForeignKey('Encuesta')
	especie 		= models.ForeignKey('Especie')
	tipo 			= models.ForeignKey('TipoCultivo')
	nroSiembra 		= models.IntegerField()
	mesSiembra 		= models.IntegerField()
	surcos 			= models.IntegerField()
	distancias 		= models.IntegerField()
	largo 			= models.IntegerField()
	tipoProducion 	= models.ForeignKey('TipoProduccion')
	eleccionCultivo = models.ForeignKey('EleccionCultivo')
	creado			= models.DateField(default=None)
	modificado 		= models.DateField(default=None)
	eliminado 		= models.DateField(default=None)

	class Meta:
		db_table = 'cultivo'

class AgroquimicoUsado(models.Model):
	encuesta 			= models.ForeignKey('Encuesta')
	producto 			= models.CharField(max_length=50)
	plaga 				= models.CharField(max_length=50)
	metodo_aplicacion 	= models.CharField(max_length=50)
	frecuencia_uso 		= models.CharField(max_length=50)
	creado				= models.DateField(default=None)
	modificado 			= models.DateField(default=None)
	eliminado 			= models.DateField(default=None)

	class Meta:
		db_table = 'agroquimico_usado'
