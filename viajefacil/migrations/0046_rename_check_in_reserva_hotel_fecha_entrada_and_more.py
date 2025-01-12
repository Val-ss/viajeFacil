# Generated by Django 5.0 on 2024-06-24 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0045_hotel_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva_hotel',
            old_name='check_in',
            new_name='fecha_entrada',
        ),
        migrations.RenameField(
            model_name='reserva_hotel',
            old_name='check_out',
            new_name='fecha_salida',
        ),
        migrations.RenameField(
            model_name='reserva_hotel',
            old_name='nombre',
            new_name='nombre_cliente',
        ),
        migrations.AddField(
            model_name='reserva_hotel',
            name='email_cliente',
            field=models.EmailField(default='email', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva_hotel',
            name='numero_habitaciones',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva_hotel',
            name='numero_huespedes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva_hotel',
            name='telefono_cliente',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
