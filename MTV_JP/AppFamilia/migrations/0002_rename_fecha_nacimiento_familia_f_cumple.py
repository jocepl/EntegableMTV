# Generated by Django 4.1 on 2022-09-13 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamilia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familia',
            old_name='Fecha_nacimiento',
            new_name='f_cumple',
        ),
    ]
