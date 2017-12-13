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

class UpdatesFromMobileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpdatesFromMobile
        fields = '__all__'            

class EstablecimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establecimiento
        fields = '__all__'

class EncuestadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encuestado
        fields = '__all__'

class FamiliaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Familia
        fields = '__all__'

class AgroquimicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agroquimico
        fields = '__all__'

class RegimenTenenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegimenTenencia
        fields = '__all__'


class NacionalidadSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Nacionalidad
        fields = '__all__'

class NivelInstruccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = NivelInstruccion
        fields = '__all__'

class FactorClimaticoSerializer(serializers.ModelSerializer):

    class Meta:
        model = FactorClimatico
        fields = '__all__'

class TripleLavadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TripleLavado
        fields = '__all__'

class AsesoramientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asesoramiento
        fields = '__all__'


class EncuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encuesta
        fields = '__all__'

class InvernaculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invernaculo
        fields = '__all__'

class MaterialEstructuraSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialEstructura
        fields = '__all__'

class AnioConstruccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnioConstruccion
        fields = '__all__'

class CultivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cultivo
        fields = '__all__'

class EspecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especie
        fields = '__all__'

class TipoCultivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoCultivo
        fields = '__all__'

class TipoProduccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoProduccion
        fields = '__all__'

class EleccionCultivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EleccionCultivo
        fields = '__all__'

class AgroquimicoUsadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgroquimicoUsado
        fields = '__all__'

class IdsTransaccionSerializer(serializers.Serializer):

    establecimiento = serializers.IntegerField()
    encuestado      = serializers.IntegerField()
    familia         = serializers.IntegerField()
    agroquimico     = serializers.IntegerField()