from model_utils.models import TimeStampedModel
from django.db import models
from ..account.models import Account
from ..pedidos.models import Pedidos

class Chat(TimeStampedModel):

    class Meta:
        verbose_name = 'ChatPeeedido'
        verbose_name_plural = 'ChatPedido'

    msg = models.CharField(max_length=100)
    account = models.ForeignKey(
        Account,
        verbose_name='Account_chat',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    pedido = models.ForeignKey(
        Pedidos,
        verbose_name='Pedidos_chat',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.msg