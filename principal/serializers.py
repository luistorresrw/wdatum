from django.contrib.auth.models import User, Group
from rest_framework import serializers
from principal.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')



class UpdatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Updates
        fields = ('id','entidad','id_entidad','valor')

class EstablecimientoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Establecimiento
        fields = '__all__'

class EncuestadoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Encuestado
        fields = '__all__'

class FamiliaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Familia
        fields = '__all__'

class AgroquimicoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Agroquimico
        fields = '__all__'

class RegimenTenenciaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RegimenTenencia
        fields = '__all__'


class NacionalidadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model =  Nacionalidad
        fields = '__all__'

class NivelInstruccionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NivelInstruccion
        fields = '__all__'

class FactorClimaticoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FactorClimatico
        fields = '__all__'

class TripleLavadoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TripleLavado
        fields = '__all__'

class AsesoramientoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Asesoramiento
        fields = '__all__'


class EncuestaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Encuesta
        fields = '__all__'

class InvernaculoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Invernaculo
        fields = '__all__'

class MaterialEstructuraSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MaterialEstructura
        fields = '__all__'

class AnioConstruccionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AnioConstruccion
        fields = '__all__'

class CultivoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cultivo
        fields = '__all__'

class EspecieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Especie
        fields = '__all__'

class TipoCultivoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TipoCultivo
        fields = '__all__'

class TipoProduccionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TipoProduccion
        fields = '__all__'

class EleccionCultivoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EleccionCultivo
        fields = '__all__'

class AgroquimicoUsadoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AgroquimicoUsado
        fields = '__all__'
