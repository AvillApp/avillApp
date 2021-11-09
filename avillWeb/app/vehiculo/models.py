from model_utils.models import TimeStampedModel
from django.db import models
from ..servicios.models import Servicios
from ..account.models import Account, Photo


class Vehiculo(TimeStampedModel):
    name = models.CharField('Nombre', max_length=250, blank=True)
    placa = models.CharField('Placa', max_length=100, unique=True)
    modelo = models.CharField('Modelo', max_length=100, blank=True)
    marca = models.CharField('Marca', max_length=100, blank=True)
    vigencia = models.DateField('Vigencia', max_length=100, blank=True)
    photo = models.ForeignKey(
        Photo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='photo_vehiculo'
    )
    estado = models.BooleanField('Estado', default=False)
    servicio = models.ForeignKey(
        Servicios,
        related_name="Servicios",
        on_delete=models.CASCADE
    )
    persona = models.ForeignKey(
        Account,
        related_name='vehiculo_persona',
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.name) + " " + str(self.placa) + " " + str(self.servicio)
