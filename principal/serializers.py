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
        model = establecimiento
        fields = '__all__'
