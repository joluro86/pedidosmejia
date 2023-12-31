# Generated by Django 4.0.6 on 2023-08-10 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0013_alter_pedido_numero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='id_acta',
            new_name='acta',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='id_actividad',
            new_name='actividad',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='id_oficial',
            new_name='oficial',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0, message='Este campo debe tener 8 dígitos.'), django.core.validators.MaxValueValidator(99999999, message='Este campo debe tener 8 dígitos.'), django.core.validators.RegexValidator('^\\d{8}$', message='Este campo debe tener exactamente 8 dígitos.')]),
        ),
    ]
