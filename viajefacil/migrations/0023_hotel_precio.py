# Generated by Django 5.0 on 2024-06-21 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0022_alter_hotel_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='precio',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=10),
            preserve_default=False,
        ),
    ]
