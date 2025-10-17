"""
Bloque de rutas web (templates) para CRUD fuera del admin por cada entidad exigida.
"""
from django.urls import path
from . import views as v

urlpatterns = [
    # Inicio (home)
    path('', v.HomeView.as_view(), name='home'),
    # Especialidad
    path('especialidades/', v.EspecialidadListView.as_view(), name='esp_list'),
    path('especialidades/nuevo/', v.EspecialidadCreateView.as_view(), name='esp_create'),
    path('especialidades/<int:pk>/editar/', v.EspecialidadUpdateView.as_view(), name='esp_update'),
    path('especialidades/<int:pk>/eliminar/', v.EspecialidadDeleteView.as_view(), name='esp_delete'),

    # Paciente
    path('pacientes/', v.PacienteListView.as_view(), name='pac_list'),
    path('pacientes/nuevo/', v.PacienteCreateView.as_view(), name='pac_create'),
    path('pacientes/<int:pk>/editar/', v.PacienteUpdateView.as_view(), name='pac_update'),
    path('pacientes/<int:pk>/eliminar/', v.PacienteDeleteView.as_view(), name='pac_delete'),

    # Medico
    path('medicos/', v.MedicoListView.as_view(), name='med_list'),
    path('medicos/nuevo/', v.MedicoCreateView.as_view(), name='med_create'),
    path('medicos/<int:pk>/editar/', v.MedicoUpdateView.as_view(), name='med_update'),
    path('medicos/<int:pk>/eliminar/', v.MedicoDeleteView.as_view(), name='med_delete'),

    # Tratamiento
    path('tratamientos/', v.TratamientoListView.as_view(), name='trat_list'),
    path('tratamientos/nuevo/', v.TratamientoCreateView.as_view(), name='trat_create'),
    path('tratamientos/<int:pk>/editar/', v.TratamientoUpdateView.as_view(), name='trat_update'),
    path('tratamientos/<int:pk>/eliminar/', v.TratamientoDeleteView.as_view(), name='trat_delete'),

    # Medicamento
    path('medicamentos/', v.MedicamentoListView.as_view(), name='medic_list'),
    path('medicamentos/nuevo/', v.MedicamentoCreateView.as_view(), name='medic_create'),
    path('medicamentos/<int:pk>/editar/', v.MedicamentoUpdateView.as_view(), name='medic_update'),
    path('medicamentos/<int:pk>/eliminar/', v.MedicamentoDeleteView.as_view(), name='medic_delete'),

    # Consulta médica
    path('consultas/', v.ConsultaMedicaListView.as_view(), name='cons_list'),
    path('consultas/nuevo/', v.ConsultaMedicaCreateView.as_view(), name='cons_create'),
    path('consultas/<int:pk>/editar/', v.ConsultaMedicaUpdateView.as_view(), name='cons_update'),
    path('consultas/<int:pk>/eliminar/', v.ConsultaMedicaDeleteView.as_view(), name='cons_delete'),

    # Receta médica
    path('recetas/', v.RecetaMedicaListView.as_view(), name='rec_list'),
    path('recetas/nuevo/', v.RecetaMedicaCreateView.as_view(), name='rec_create'),
    path('recetas/<int:pk>/editar/', v.RecetaMedicaUpdateView.as_view(), name='rec_update'),
    path('recetas/<int:pk>/eliminar/', v.RecetaMedicaDeleteView.as_view(), name='rec_delete'),

    # Citas
    path('citas/', v.CitaListView.as_view(), name='cita_list'),
    path('citas/nuevo/', v.CitaCreateView.as_view(), name='cita_create'),
    path('citas/<int:pk>/editar/', v.CitaUpdateView.as_view(), name='cita_update'),
    path('citas/<int:pk>/eliminar/', v.CitaDeleteView.as_view(), name='cita_delete'),
]
