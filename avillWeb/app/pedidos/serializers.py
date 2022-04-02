from django.forms import IntegerField
from rest_framework import serializers
from rest_framework.relations import ManyRelatedField
from .models import Pedidos, PedidosActivid, RatingAccount, RatingPedido
from ..vehiculo.serializers import VehiculoSerializer
from ..account.serializers import AccountSerializer


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


class RatingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingAccount
        fields = ('__all__')


class RatingPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingPedido
        fields = ('__all__')
