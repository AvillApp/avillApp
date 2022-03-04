from model_utils.models import TimeStampedModel
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from ..account.models import Account, Estado
from ..vehiculo.models import Vehiculo


class Pedidos(TimeStampedModel):

    class Meta:
        verbose_name = 'Pedidos'
        verbose_name_plural = 'Pedidos'

    emision = models.CharField(
        'Recogida', max_length=256, null=True, blank=True)
    destino = models.CharField(
        'Destino', max_length=256, null=True, blank=True)
    indicacion = models.CharField(
        'Indicacion',  max_length=256, null=True, blank=True)
    longitude = models.CharField(
        'Longitude',  max_length=100, null=True, blank=True)
    latitude = models.CharField(
        'Latitude',  max_length=100, null=True, blank=True)
    telealt = models.BigIntegerField(
        'Telefono alternativo', null=True, blank=True)
    tiempo = models.IntegerField('Tiempo', null=True, blank=True)
    precio = models.BigIntegerField('Precio', null=True, blank=True)
    solicitud = models.CharField(
        'Serivicio_solicitud', max_length=100, null=True, blank=True)

    estado = models.ForeignKey(
        Estado,
        verbose_name='Estado_pedido',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    account = models.ForeignKey(
        Account,
        verbose_name='Account_pedido',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    vehiculo = models.ForeignKey(
        Vehiculo,
        verbose_name='Vehiculo_pedido',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.emision) + " " + str(self. destino)


class PedidosActivid(TimeStampedModel):
    class Meta:
        verbose_name = 'Actividades Pedido'
        verbose_name_plural = 'Actividades Pedido'

    title = models.CharField('Titulo', max_length=100)
    description = models.CharField('Descripcion', max_length=100, blank=True)
    time = models.TimeField('Tiempo', auto_now_add=True)
    fecha = models.DateField('Fecha', auto_now_add=True)
    pedido = models.ForeignKey(
        Pedidos,
        verbose_name='Pedido',
        on_delete=models.CASCADE
    )
    realizado_by = models.ForeignKey(
        Account,
        verbose_name='Realizado por',
        on_delete=models.CASCADE
    )


class RatingAccount(TimeStampedModel):
    class Meta:
        verbose_name = 'RatingAccount'
        verbose_name_plural = 'RatingAccount'
    puntos = models.IntegerField('Puntos', default=0, blank=True, null=True)
    obs = models.CharField('Observación', max_length=255,
                           blank=True, null=True)
    account = models.ForeignKey(
        Account,
        verbose_name='RatingAccount',
        on_delete=models.CASCADE
    )
    realizado_by = models.ForeignKey(
        Account,
        verbose_name='Realizado por',
        related_name='Realizado_por',
        on_delete=models.CASCADE
    )


class RatingPedido(TimeStampedModel):
    class Meta:
        verbose_name = 'RatingPedido'
        verbose_name_plural = 'RatingPedido'
    puntos = models.IntegerField('Puntos', default=0, blank=True, null=True)
    obs = models.CharField('Observación', max_length=255,
                           blank=True, null=True)
    pedido = models.ForeignKey(
        Pedidos,
        verbose_name='RatingPedido',
        on_delete=models.CASCADE
    )
    realizado_by = models.ForeignKey(
        Account,
        verbose_name='Realizado por',
        on_delete=models.CASCADE
    )


@receiver(post_save, sender=RatingAccount)
def set_puntos(sender, instance, created, **kwargs):

    if created:
        suma = instance.puntos + instance.account.puntos
        prom = suma / 2
        instance.account.puntos = prom
        instance.account.save()
