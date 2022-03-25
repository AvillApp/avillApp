from rest_framework import viewsets
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import VehiculoSerializer


class VehiculoViewset(viewsets.ModelViewSet):

    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ["=servicio__nombre"]
    ordering_fields = ('__all__')
