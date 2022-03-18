from rest_framework import serializers
from .models import Vehiculo
from ..account.serializers import AccountSerializer
from ..servicios.serializers import ServiciosSerializer


class VehiculoSerializer(serializers.ModelSerializer):
    persona = AccountSerializer(required=False)
    persona_id = serializers.IntegerField(required=False)
    placa= serializers.CharField(required=False)
    servicio= ServiciosSerializer(required=False)
    servicio_id = serializers.IntegerField(required=False)


    class Meta:
        model = Vehiculo
        fields = ('__all__')
