"""
Bloque de Views DRF (API) y CBVs (web) con comentarios en bloque.
- API: ViewSets con filtros y búsqueda (django-filter, SearchFilter).
- Web: Vistas genéricas para CRUD con templates y footer requerido.
"""
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Especialidad, Paciente, Medico, Tratamiento, Medicamento,
    ConsultaMedica, RecetaMedica, RecetaItem, Cita
)
from .serializers import (
    EspecialidadSerializer, PacienteSerializer, MedicoSerializer,
    TratamientoSerializer, MedicamentoSerializer, ConsultaMedicaSerializer,
    RecetaMedicaSerializer, RecetaItemSerializer, CitaSerializer
)

# -------------------- API (DRF) --------------------
class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['nombre']

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['sexo']
    search_fields = ['nombre', 'RUT']
    ordering_fields = ['nombre']

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.select_related('especialidad').all()
    serializer_class = MedicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['especialidad']
    search_fields = ['nombre', 'RUT', 'especialidad__nombre']
    ordering_fields = ['nombre']

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.select_related('paciente', 'medico').all()
    serializer_class = ConsultaMedicaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['medico', 'paciente', 'medico__especialidad']
    search_fields = ['motivo', 'diagnostico', 'paciente__nombre', 'medico__nombre']

class RecetaMedicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.prefetch_related('items').all()
    serializer_class = RecetaMedicaSerializer

class RecetaItemViewSet(viewsets.ModelViewSet):
    queryset = RecetaItem.objects.select_related('receta', 'medicamento').all()
    serializer_class = RecetaItemSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.select_related('paciente', 'medico', 'consulta').all()
    serializer_class = CitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['medico', 'paciente', 'estado']
    search_fields = ['paciente__nombre', 'medico__nombre']
    ordering_fields = ['fecha_hora']

# -------------------- Web (templates) --------------------
# Nota: Todas las templates heredarán un base con footer de nombre, sección y año.

class HomeView(TemplateView):
    template_name = 'clinica/home.html'

class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'clinica/list_generic.html'
    extra_context = {'headers': ['ID', 'Nombre'], 'fields': ['id', 'nombre']}

class EspecialidadCreateView(CreateView):
    model = Especialidad
    fields = ['nombre']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('esp_list')

class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    fields = ['nombre']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('esp_list')

class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = 'clinica/confirm_delete.html'
    success_url = reverse_lazy('esp_list')

class PacienteListView(ListView):
    model = Paciente
    template_name = 'clinica/list_generic.html'
    extra_context = {'headers': ['ID', 'RUT', 'Nombre', 'Nacimiento', 'Sexo'], 'fields': ['id', 'RUT', 'nombre', 'fecha_nacimiento', 'sexo']}

class PacienteCreateView(CreateView):
    model = Paciente
    fields = ['RUT', 'nombre', 'fecha_nacimiento', 'sexo']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('pac_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['RUT', 'nombre', 'fecha_nacimiento', 'sexo']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('pac_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'clinica/confirm_delete.html'
    success_url = reverse_lazy('pac_list')

class MedicoListView(ListView):
    model = Medico
    template_name = 'clinica/list_generic.html'
    extra_context = {'headers': ['ID', 'RUT', 'Nombre', 'Especialidad'], 'fields': ['id', 'RUT', 'nombre', 'especialidad']}

class MedicoCreateView(CreateView):
    model = Medico
    fields = ['RUT', 'nombre', 'especialidad']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('med_list')

class MedicoUpdateView(UpdateView):
    model = Medico
    fields = ['RUT', 'nombre', 'especialidad']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('med_list')

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'clinica/confirm_delete.html'
    success_url = reverse_lazy('med_list')

class TratamientoListView(ListView):
    model = Tratamiento
    template_name = 'clinica/list_generic.html'
    extra_context = {'headers': ['ID', 'Nombre', 'Descripción'], 'fields': ['id', 'nombre', 'descripcion']}

class TratamientoCreateView(CreateView):
    model = Tratamiento
    fields = ['nombre', 'descripcion']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('trat_list')

class TratamientoUpdateView(UpdateView):
    model = Tratamiento
    fields = ['nombre', 'descripcion']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('trat_list')

class TratamientoDeleteView(DeleteView):
    model = Tratamiento
    template_name = 'clinica/confirm_delete.html'
    success_url = reverse_lazy('trat_list')

class MedicamentoListView(ListView):
    model = Medicamento
    template_name = 'clinica/list_generic.html'
    extra_context = {'headers': ['ID', 'Nombre', 'Descripción'], 'fields': ['id', 'nombre', 'descripcion']}

class MedicamentoCreateView(CreateView):
    model = Medicamento
    fields = ['nombre', 'descripcion']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('medic_list')

class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    fields = ['nombre', 'descripcion']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('medic_list')

class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = 'clinica/confirm_delete.html'
    success_url = reverse_lazy('medic_list')

class ConsultaMedicaListView(ListView):
    model = ConsultaMedica
    template_name = 'clinica/list_generic.html'
    extra_context = {'headers': ['ID', 'Paciente', 'Médico', 'Fecha', 'Motivo'], 'fields': ['id', 'paciente', 'medico', 'fecha', 'motivo']}

class ConsultaMedicaCreateView(CreateView):
    model = ConsultaMedica
    fields = ['paciente', 'medico', 'fecha', 'motivo', 'diagnostico', 'tratamiento']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('cons_list')

class ConsultaMedicaUpdateView(UpdateView):
    model = ConsultaMedica
    fields = ['paciente', 'medico', 'fecha', 'motivo', 'diagnostico', 'tratamiento']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('cons_list')

class ConsultaMedicaDeleteView(DeleteView):
    model = ConsultaMedica
    template_name = 'clinica/confirm_delete.html'
    success_url = reverse_lazy('cons_list')

class RecetaMedicaListView(ListView):
    model = RecetaMedica
    template_name = 'clinica/list_generic.html'
    extra_context = {'headers': ['ID', 'Consulta', 'Indicaciones'], 'fields': ['id', 'consulta', 'indicaciones']}

class RecetaMedicaCreateView(CreateView):
    model = RecetaMedica
    fields = ['consulta', 'indicaciones']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('rec_list')

class RecetaMedicaUpdateView(UpdateView):
    model = RecetaMedica
    fields = ['consulta', 'indicaciones']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('rec_list')

class RecetaMedicaDeleteView(DeleteView):
    model = RecetaMedica
    template_name = 'clinica/confirm_delete.html'
    success_url = reverse_lazy('rec_list')

class CitaListView(ListView):
    model = Cita
    template_name = 'clinica/list_generic.html'
    extra_context = {'headers': ['ID', 'Paciente', 'Médico', 'Fecha y Hora', 'Estado'], 'fields': ['id', 'paciente', 'medico', 'fecha_hora', 'estado']}

class CitaCreateView(CreateView):
    model = Cita
    fields = ['paciente', 'medico', 'fecha_hora', 'estado', 'consulta']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('cita_list')

class CitaUpdateView(UpdateView):
    model = Cita
    fields = ['paciente', 'medico', 'fecha_hora', 'estado', 'consulta']
    template_name = 'clinica/form_generic.html'
    success_url = reverse_lazy('cita_list')

class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'clinica/confirm_delete.html'
    success_url = reverse_lazy('cita_list')
