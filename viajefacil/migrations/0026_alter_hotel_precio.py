# Generated by Django 5.0 on 2024-06-21 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0025_alter_hotel_precio_alter_reserva_hotel_tarifa_noche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='precio',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
