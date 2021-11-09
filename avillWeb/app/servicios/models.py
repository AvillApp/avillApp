from model_utils.models import TimeStampedModel
from django.db import models


class Type_servicios(TimeStampedModel):

    class Meta:
        verbose_name = 'Tipo de servicios'
        verbose_name_plural = 'Tipo de servicios'

    nombre = models.CharField('Nombre', max_length=90)

    def __str__(self):
        return str(self.nombre)


class Servicios(TimeStampedModel):

    class Meta:
        verbose_name = 'Servicios'
        verbose_name_plural = 'Servicios'

    type_servicios = models.ForeignKey(
        Type_servicios,
        verbose_name="type_servicios",
        on_delete=models.CASCADE
    )
    nombre = models.CharField('Nombre', max_length=255, blank=True)

    def __str__(self):
        return str(self.nombre)
