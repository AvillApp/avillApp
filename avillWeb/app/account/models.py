from model_utils.models import TimeStampedModel

from django.db import models


class TypeEstado(TimeStampedModel):
    name = models.CharField('Estado', max_length=50)

    def __str__(self):
        return self.name


class Estado(TimeStampedModel):
    name = models.CharField('Estado', max_length=50)
    ayuda = models.CharField('Ayuda', max_length=256, blank=True)
    type_estado = models.ForeignKey(
        TypeEstado, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Type_Account(TimeStampedModel):

    class Meta:
        verbose_name = 'Tipos de Account'

    name = models.CharField('Nombre', max_length=100)

    def __str__(self):
        return str(self.name)


class Photo(TimeStampedModel):
    title = models.CharField(max_length=100)
    photo = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title

# class DevicePush()


class Account(TimeStampedModel):

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    identidy = models.BigIntegerField(
        'Identificacion', null=True, default=0, blank=True)
    name = models.CharField('Nombre', max_length=100, blank=True)
    last_name = models.CharField('Apellidos', max_length=100, blank=True)
    email = models.EmailField('Email', blank=True)
    phone = models.BigIntegerField('Teléfono', unique=True)
    password = models.CharField(
        'Contraseña', max_length=100, blank=True, null=True)
    photo = models.ForeignKey(
        Photo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='photo_account'
    )
    type_persona = models.ForeignKey(
        Type_Account,
        verbose_name="Type account",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=1,
    )
    estado = models.ForeignKey(
        Estado,
        verbose_name='Estado_account',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=1
    )
    tokenPush = models.CharField(
        'TokenPush', null=True, blank=True, max_length=256)
    puntos = models.FloatField('Puntos', default=1, blank=True, null=True)

    def __str__(self):
        return str(self.name) + " " + str(self.last_name) + " " + str(self.phone)
