# Generated by Django 5.0 on 2024-06-25 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0050_destino_ubicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='ubicacion',
        ),
    ]
