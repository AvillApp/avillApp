from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView,
)
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *


class PedidosViewset(viewsets.ModelViewSet):

    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ["=vehiculo__persona__id"]
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


class RatingAccountViewset(viewsets.ModelViewSet):

    queryset = RatingAccount.objects.all()
    serializer_class = RatingAccountSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class RatingPedidoViewset(viewsets.ModelViewSet):

    queryset = RatingPedido.objects.all()
    serializer_class = RatingPedidoSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class PedidoVehiculoViewset(ListAPIView):
    serializer_class = PedidosSerializer

    def get_queryset(self):
        persona = self.kwargs['persona']
        pedidos = Pedidos.objects.filter(
            vehiculo__persona=persona,
            estado=7
        ).order_by('-id')[0:1]

        return pedidos
