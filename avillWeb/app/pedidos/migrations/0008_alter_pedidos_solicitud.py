# Generated by Django 3.2.9 on 2022-03-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_alter_pedidos_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='solicitud',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Serivicio_solicitud'),
        ),
    ]
