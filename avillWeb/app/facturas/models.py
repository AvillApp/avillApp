from model_utils.models import TimeStampedModel
from django.db import models
from ..pedidos.models import Pedidos


class Comision(TimeStampedModel):

    class Meta:
        verbose_name = 'Comisión'
        verbose_name_plural = 'Comisión'
    
    fecha_inicio = models.DateField('Fecha de inicio', blank=True, null=True)
    fecha_final =  models.DateField('Fecha de vencimiento', blank=True, null=True)
    valor = models.IntegerField('%Porcentaje', blank=True, null=True)
    estado = models.BooleanField('Estado', default=True)

    def __str__(self):
        return str(self.valor) + " " + str(self.fecha_inicio)

class Factura(TimeStampedModel):

    class Meta:
        verbose_name = 'Facturas'
        verbose_name_plural = 'Facturas'

    precio = models.IntegerField('Valor')
    fecha_pago = models.DateField('Fecha de Pago', blank=True, null=True)
    pedido = models.OneToOneField(Pedidos, on_delete=models.CASCADE)
    comision = models.ForeignKey(
        Comision,
        verbose_name='Comision_factura',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.pedido) + " " + str(self.fecha_pago)
