# Generated by Django 3.2.9 on 2021-11-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_puntos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='puntos',
            field=models.FloatField(blank=True, default=1, null=True, verbose_name='Puntos'),
        ),
    ]
