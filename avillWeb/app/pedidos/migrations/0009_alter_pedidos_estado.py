# Generated by Django 3.2.9 on 2022-04-06 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_notify'),
        ('pedidos', '0008_alter_pedidos_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='estado',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.estado', verbose_name='Estado_pedido'),
        ),
    ]
