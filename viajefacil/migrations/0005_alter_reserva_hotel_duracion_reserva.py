# Generated by Django 5.0 on 2024-05-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0004_alter_reserva_hotel_tarifa_noche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva_hotel',
            name='duracion_reserva',
            field=models.DurationField(editable=False),
        ),
    ]