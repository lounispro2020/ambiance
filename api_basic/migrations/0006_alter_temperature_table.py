# Generated by Django 3.2.3 on 2021-06-10 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0005_alter_temperature_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='temperature',
            table='temperature',
        ),
    ]