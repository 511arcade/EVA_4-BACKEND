"""
Bloque de rutas de la API (DRF): registra ViewSets y genera endpoints REST completos.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EspecialidadViewSet, PacienteViewSet, MedicoViewSet,
    TratamientoViewSet, MedicamentoViewSet, ConsultaMedicaViewSet,
    RecetaMedicaViewSet, RecetaItemViewSet, CitaViewSet
)

router = DefaultRouter()
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'consultas', ConsultaMedicaViewSet)
router.register(r'recetas', RecetaMedicaViewSet)
router.register(r'receta-items', RecetaItemViewSet)
router.register(r'citas', CitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
