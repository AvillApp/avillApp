from rest_framework import serializers
from .models import Account, Photo, Notify


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(required=False)
    phone = serializers.CharField(required=False)
    tokenPush = serializers.CharField(required=False)
    puntos = serializers.IntegerField(required=False)
    latitiude = serializers.CharField(required=False)
    longitude = serializers.CharField(required=False)
    photo_id = serializers.IntegerField(required=False)

    class Meta:
        model = Account
        fields = '__all__'

class NotifySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notify
        fields = '__all__'