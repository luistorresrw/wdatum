from django import forms
from principal import models as principal_models
from django.contrib.auth.models import User
from django.forms import ModelForm

'''
ROL_CHOICES = (
	('Administrador', 'Administrador'),
	('Operador', 'Operador'),
	('Encuestador', 'Encuestador'),
)
'''

class UsuarioForm(forms.ModelForm):
	#username = forms.CharField(widget=forms.TextInput())
	#last_name = forms.CharField(widget=forms.TextInput())
	#first_name = forms.CharField(widget=forms.TextInput())
	#email = forms.EmailField(widget=forms.TextInput())
	
	#dni = forms.CharField(widget=forms.TextInput())
	#rol = forms.CharField(widget = forms.Select(choices = ROL_CHOICES))
	
	username = forms.EmailField(widget=forms.TextInput())

	class Meta:
		model = principal_models.Usuario
		exclude = ('email','is_staff','last_login', 'password', 'date_joined', 'is_active','groups','user_permissions','is_superuser')

  
class NacionalidadForm(forms.ModelForm):
	class Meta:
		model = principal_models.Nacionalidad
		fields = ('descripcion',)


class NivelInstruccionForm(forms.ModelForm):
	class Meta:
		model = principal_models.NivelInstruccion
		fields = ('descripcion',)


class RegimenTenenciaForm(forms.ModelForm):
	class Meta:
		model = principal_models.RegimenTenencia
		fields = ('descripcion',)


class AnioConstruccionForm(forms.ModelForm):
	class Meta:
		model = principal_models.AnioConstruccion
		fields = ('descripcion',)


class MaterialEstructuraForm(forms.ModelForm):
	class Meta:
		model = principal_models.MaterialEstructura
		fields = ('descripcion',)


class TipoProduccionForm(forms.ModelForm):
	class Meta:
		model = principal_models.TipoProduccion
		fields = ('descripcion',)


class EleccionCultivoForm(forms.ModelForm):
	class Meta:
		model = principal_models.EleccionCultivo
		fields = ('descripcion',)


class TipoCultivoForm(forms.ModelForm):
	class Meta:
		model = principal_models.TipoCultivo
		fields = ('descripcion',)


class EspecieForm(forms.ModelForm):
	class Meta:
		model = principal_models.Especie
		fields = ('descripcion',)


class FactorClimaticoForm(forms.ModelForm):
	class Meta:
		model = principal_models.FactorClimatico
		fields = ('descripcion',)


class TripleLavadoForm(forms.ModelForm):
	class Meta:
		model = principal_models.TripleLavado
		fields = ('descripcion',)


class AsesoramientoForm(forms.ModelForm):
	class Meta:
		model = principal_models.Asesoramiento
		fields = ('descripcion',)