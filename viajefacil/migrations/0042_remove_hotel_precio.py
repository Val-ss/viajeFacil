# Generated by Django 5.0 on 2024-06-21 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0041_alter_reserva_hotel_tarifa_noche'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='precio',
        ),
    ]