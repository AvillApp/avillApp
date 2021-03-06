# Generated by Django 3.2.9 on 2021-11-20 11:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_puntos'),
        ('pedidos', '0003_auto_20211108_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('puntos', models.IntegerField(blank=True, default=0, null=True, verbose_name='Puntos')),
                ('obs', models.CharField(max_length=255, verbose_name='Observación')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedidos', verbose_name='RatingPedido')),
                ('realizado_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account', verbose_name='Realizado por')),
            ],
            options={
                'verbose_name': 'RatingPedido',
                'verbose_name_plural': 'RatingPedido',
            },
        ),
        migrations.CreateModel(
            name='RatingAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('puntos', models.IntegerField(blank=True, default=0, null=True, verbose_name='Puntos')),
                ('obs', models.CharField(max_length=255, verbose_name='Observación')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account', verbose_name='RatingAccount')),
                ('realizado_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Realizado_por', to='account.account', verbose_name='Realizado por')),
            ],
            options={
                'verbose_name': 'RatingAccount',
                'verbose_name_plural': 'RatingAccount',
            },
        ),
    ]
