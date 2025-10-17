from django.contrib import admin
from .models import Especialidad, Paciente, Medico, Tratamiento, Medicamento, ConsultaMedica, RecetaMedica, RecetaItem, Cita

admin.site.register(Especialidad)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Tratamiento)
admin.site.register(Medicamento)
admin.site.register(ConsultaMedica)
admin.site.register(RecetaMedica)
admin.site.register(RecetaItem)
admin.site.register(Cita)
