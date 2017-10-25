from django import forms
from principal import models as principal_models


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