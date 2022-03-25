from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, Photo, Notify
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AccountSerializer, PhotoSerializer, NotifySerializer


class AccountViewset(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ['=identidy', '=name', '=last_name', '=phone']
    ordering_fields = ('__all__')

class PhotoViewset(viewsets.ModelViewSet):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')

class NotifyViewset(viewsets.ModelViewSet):
    
    queryset = Notify.objects.all()
    serializer_class = NotifySerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')