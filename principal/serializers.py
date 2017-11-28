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

class RegimenTenenciaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RegimenTenencia
        fields = ('url','descripcion')

class UpdatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Updates
        fields = ('id','entidad','id_entidad','valor')

class EstablecimientoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Establecimiento
        fields = ('url','nombre','numero','posLatitud','posLongitud','foto','regimenTenencia','regimenOtros')

class EncuestadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encuestado
        fields = '__all__'
