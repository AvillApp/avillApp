# Generated by Django 3.2.9 on 2021-11-09 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculo_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculo',
            old_name='photo',
            new_name='photovehi',
        ),
    ]