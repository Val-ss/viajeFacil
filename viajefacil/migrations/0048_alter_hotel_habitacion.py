# Generated by Django 5.0 on 2024-06-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0047_alter_hotel_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='habitacion',
            field=models.IntegerField(),
        ),
    ]