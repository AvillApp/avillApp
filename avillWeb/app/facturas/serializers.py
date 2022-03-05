from rest_framework import serializers
from .models import Factura, Comision

from ..pedidos.serializers import PedidosSerializer


class ComisionSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Comision
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    pedido = PedidosSerializer(required=False)
    fecha_pago  = serializers.CharField(required=False)
    pedido_id  = serializers.IntegerField(required=False)
    comision_id  = serializers.IntegerField(required=False)
    
    class Meta:
        model = Factura
        fields = ('__all__')