# Generated by Django 3.2.9 on 2021-11-09 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo_vehiculo', to='account.photo'),
        ),
    ]
