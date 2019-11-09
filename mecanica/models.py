from django.db import models
from django.utils import timezone
from django.contrib import admin

class Propietario(models.Model):
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    nombre1 = models.CharField(max_length=15)
    nombre2 = models.CharField(max_length=15)
    dpi = models.CharField(max_length=15)
    telefono = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    fecha_registro = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return '%s %s %s %s' % (self.nombre1, self.nombre2, self.apellido_paterno, self.apellido_materno)
    
class Auto(models.Model):
    nombre_propietario  = models.ForeignKey(Propietario, on_delete= models.CASCADE)
    placas = models.CharField(max_length=10)
    modelo = models.CharField(max_length=30)
    anio = models.DateField()
    fecha_registro = models.DateTimeField(
            default=timezone.now)

#    def only_year(self):
#        return self.modelo.strftime('%Y')

    def __str__(self):
        return self.placas

class Mecanico(models.Model):
    nombre = models.CharField(max_length=35)
    nacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    especialidad = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    auto_placas = models.ForeignKey(Auto, on_delete=models.CASCADE)
    #mecanico_asignado_nombre = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    fecha = models.DateTimeField(
            default=timezone.now)
    trabajo_descripcion = models.TextField()
    costo_total = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    ESTADOS = (('T', 'Trabajando'), ('E', 'Entregado'), ('S', 'Suspendido'))
    estado = models.CharField(max_length=1, choices=ESTADOS, default='T')
    mecanicos   = models.ManyToManyField(Mecanico, through='Trabajo_mecanico')

    def __str__(self):
        return self.trabajo_descripcion



class Trabajo_mecanico(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)

class Repuesto(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    repuesto = models.CharField(max_length=30)
    existencia = models.IntegerField()
    costo_unitario = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.repuesto

class TrabajoMecanicoInLine(admin.TabularInline):
    model = Trabajo_mecanico
    extra = 1

class MecanicoAdmin(admin.ModelAdmin):
    inlines = (TrabajoMecanicoInLine,)

class TrabajoAdmin(admin.ModelAdmin):
    inlines = (TrabajoMecanicoInLine,)