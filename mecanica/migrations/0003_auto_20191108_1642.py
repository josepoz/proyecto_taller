# Generated by Django 2.2.7 on 2019-11-08 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mecanica', '0002_auto_20191106_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecanico',
            name='especialidad',
            field=models.CharField(max_length=25),
        ),
    ]
