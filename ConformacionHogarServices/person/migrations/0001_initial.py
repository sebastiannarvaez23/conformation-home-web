# Generated by Django 4.1.3 on 2022-11-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('first_name', models.CharField(max_length=200, verbose_name='Primer Nombre')),
                ('second_name', models.CharField(max_length=200, verbose_name='Segundo Nombre')),
                ('first_last_name', models.CharField(max_length=200, verbose_name='Primer Apellido')),
                ('second_last_name', models.CharField(max_length=200, verbose_name='Segundo Apellido')),
                ('date_birth', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('type_identification', models.CharField(max_length=10, verbose_name='Tipo Identificación')),
                ('num_identification', models.CharField(max_length=200, verbose_name='Número Identificación')),
            ],
        ),
    ]
