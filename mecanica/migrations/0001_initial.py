# Generated by Django 2.2.7 on 2019-11-05 03:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placas', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=30)),
                ('anio', models.DateField()),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=12)),
                ('especialidad', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(max_length=15)),
                ('apellido_materno', models.CharField(max_length=15)),
                ('nombre1', models.CharField(max_length=15)),
                ('nombre2', models.CharField(max_length=15)),
                ('dpi', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=12)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('trabajo_descripcion', models.TextField()),
                ('costo_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estado', models.CharField(choices=[('T', 'Trabajando'), ('E', 'Entregado'), ('S', 'Suspendido')], default='T', max_length=1)),
                ('auto_placas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecanica.Auto')),
                ('mecanico_asignado_nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecanica.Mecanico')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo_mecanico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecanica.Mecanico')),
                ('trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecanica.Trabajo')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repuesto', models.CharField(max_length=30)),
                ('existencia', models.IntegerField()),
                ('costo_unitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecanica.Trabajo')),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='nombre_propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecanica.Propietario'),
        ),
    ]