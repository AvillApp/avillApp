from model_utils.models import TimeStampedModel
from django.db import models
from ..pedidos.models import Pedidos


class Factura(TimeStampedModel):

    class Meta:
        verbose_name = 'Facturas'
        verbose_name_plural = 'Facturas'

    precio = models.BigIntegerField('Valor')
    fecha_factura = models.DateField('Fecha de factura')
    fecha_pago = models.DateField('Fecha de Pago')
    pedido = models.OneToOneField(Pedidos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pedido) + " " + str(self.fecha_pago)
