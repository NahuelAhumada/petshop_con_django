# Generated by Django 5.0.4 on 2024-07-04 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_marca_remove_producto_animal_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Envios',
            new_name='Envio',
        ),
    ]
