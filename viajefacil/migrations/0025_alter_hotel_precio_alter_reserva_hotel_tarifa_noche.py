# Generated by Django 5.0 on 2024-06-21 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0024_alter_reserva_hotel_tarifa_noche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='reserva_hotel',
            name='tarifa_noche',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
