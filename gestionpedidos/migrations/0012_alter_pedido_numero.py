# Generated by Django 4.0.6 on 2023-08-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0011_alter_pedido_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='numero',
            field=models.IntegerField(),
        ),
    ]