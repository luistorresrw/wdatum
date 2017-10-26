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