# Generated by Django 5.0 on 2024-06-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0046_rename_check_in_reserva_hotel_fecha_entrada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='precio',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
