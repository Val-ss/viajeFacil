# Generated by Django 5.0 on 2024-05-24 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0008_reserva_hotel_fin_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva_hotel',
            name='duracion_reserva',
            field=models.DurationField(),
        ),
    ]