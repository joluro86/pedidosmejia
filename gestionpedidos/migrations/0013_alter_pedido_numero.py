# Generated by Django 4.0.6 on 2023-08-10 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0012_alter_pedido_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='numero',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Este campo debe tener 8 dígitos.'), django.core.validators.MaxValueValidator(99999999, message='Este campo debe tener 8 dígitos.'), django.core.validators.RegexValidator('^\\d{8}$', message='Este campo debe tener exactamente 8 dígitos.')]),
        ),
    ]
