# Generated by Django 3.2.9 on 2021-11-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_tokenpush'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='puntos',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Puntos'),
        ),
    ]
