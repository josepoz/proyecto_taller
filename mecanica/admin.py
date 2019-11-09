from django.contrib import admin
from mecanica.models import Propietario, Auto, Mecanico, MecanicoAdmin, Trabajo, TrabajoAdmin, Repuesto

admin.site.register(Propietario)
admin.site.register(Auto)
admin.site.register(Mecanico, MecanicoAdmin)
admin.site.register(Trabajo, TrabajoAdmin)
admin.site.register(Repuesto)

