from rest_framework import viewsets
from .models import Servicios, Type_servicios
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ServiciosSerializer, Type_serviciosSerializer


class ServiciosViewset(viewsets.ModelViewSet):

    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class Type_serviciosViewset(viewsets.ModelViewSet):

    queryset = Type_servicios.objects.all()
    serializer_class = Type_serviciosSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')
