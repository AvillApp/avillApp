from rest_framework import serializers
from .models import Vehiculo
from ..account.serializers import AccountSerializer


class VehiculoSerializer(serializers.ModelSerializer):
    persona = AccountSerializer()

    class Meta:
        model = Vehiculo
        fields = ('__all__')
