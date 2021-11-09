from rest_framework import serializers
from .models import Pedidos, PedidosActivid
from ..vehiculo.serializers import VehiculoSerializer


class PedidosSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer(required=False)

    class Meta:
        model = Pedidos
        fields = ('__all__')


class PedidosUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedidos
        fields = ('__all__')


class PedidosActividSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidosActivid
        fields = ('__all__')
