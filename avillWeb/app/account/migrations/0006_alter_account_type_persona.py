# Generated by Django 3.2.9 on 2022-02-20 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20211120_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='type_persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.type_account', verbose_name='Type account'),
        ),
    ]