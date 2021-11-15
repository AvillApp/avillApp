from rest_framework import serializers
from .models import Account, Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(required=False)
    phone = serializers.CharField(required=False)
    type_persona = serializers.CharField(required=False)

    class Meta:
        model = Account
        fields = '__all__'
