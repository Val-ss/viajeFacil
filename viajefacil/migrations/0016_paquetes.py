# Generated by Django 5.0 on 2024-05-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0015_remove_reserva_hotel_fin_reserva_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paquetes',
            fields=[
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
                ('traslado', models.CharField(max_length=200)),
            ],
        ),
    ]
