# Generated by Django 4.0.6 on 2022-09-13 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipos', '0004_nacionalidad_rol_tecnico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nacionalidad',
            name='Nombre',
            field=models.CharField(max_length=30, verbose_name='Nacionalidad'),
        ),
    ]
