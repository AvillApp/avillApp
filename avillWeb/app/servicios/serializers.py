from rest_framework import serializers
from .models import Servicios, Type_servicios


class Type_serviciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_servicios
        fields = ('__all__')


class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ('__all__')
