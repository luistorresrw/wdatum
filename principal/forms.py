from django import forms

from .models import Nacionalidad, NivelInstruccion

class NacionalidadForm(forms.ModelForm):
	class Meta:
		model = Nacionalidad
		fields = ('descripcion',)

class NivelInstruccionForm(forms.ModelForm):
	class Meta:
		model = NivelInstruccion
		fields = ('descripcion',)



