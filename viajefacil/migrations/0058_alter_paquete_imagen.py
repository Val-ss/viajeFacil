# Generated by Django 5.0 on 2024-07-03 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajefacil', '0057_paquete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
    ]
