# Generated by Django 3.2.13 on 2022-06-28 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='myuser',
            table='User',
        ),
    ]
