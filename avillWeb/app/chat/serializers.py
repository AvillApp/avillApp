from rest_framework import serializers
from .models import Chat
from ..account.serializers import AccountSerializer


class ChatSerializer(serializers.ModelSerializer):
    account = AccountSerializer(required=False)
    account_id = serializers.IntegerField(required=False)
    
    class Meta:
        model = Chat
        fields = '__all__'
