# Generated by Django 5.0 on 2024-06-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0048_alter_hotel_habitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva_hotel',
            name='tarifa_noche',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]