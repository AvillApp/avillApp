from django.shortcuts import render
from rest_framework import viewsets
from .models import Comision, Factura
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ComisionSerializer, FacturaSerializer


class FacturaViewset(viewsets.ModelViewSet):

    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')

class ComisionViewset(viewsets.ModelViewSet):

    queryset = Comision.objects.all()
    serializer_class = ComisionSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')