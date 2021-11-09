from rest_framework import viewsets
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PedidosSerializer, PedidosActividSerializer, PedidosUpdateSerializer


class PedidosViewset(viewsets.ModelViewSet):

    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class PedidosUpdateViewset(viewsets.ModelViewSet):

    queryset = Pedidos.objects.all()
    serializer_class = PedidosUpdateSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class PedidosActividViewset(viewsets.ModelViewSet):

    queryset = PedidosActivid.objects.all()
    serializer_class = PedidosActividSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')
