# Generated by Django 4.0.6 on 2023-08-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0004_alter_oficial_cedula'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficial',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=20),
        ),
    ]
