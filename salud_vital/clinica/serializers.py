"""
Bloque de Serializers DRF: definen cómo exponer entidades JSON.
Incluye serializers anidados para Receta con Items.
"""
from rest_framework import serializers
from .models import (
    Especialidad, Paciente, Medico, Tratamiento, Medicamento,
    ConsultaMedica, RecetaMedica, RecetaItem, Cita
)

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    especialidad_nombre = serializers.ReadOnlyField(source='especialidad.nombre')
    class Meta:
        model = Medico
        fields = ['id', 'RUT', 'nombre', 'especialidad', 'especialidad_nombre']

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.ReadOnlyField(source='paciente.nombre')
    medico_nombre = serializers.ReadOnlyField(source='medico.nombre')
    class Meta:
        model = ConsultaMedica
        fields = '__all__'

class RecetaItemSerializer(serializers.ModelSerializer):
    medicamento_nombre = serializers.ReadOnlyField(source='medicamento.nombre')
    class Meta:
        model = RecetaItem
        fields = ['id', 'medicamento', 'medicamento_nombre', 'dosis', 'frecuencia', 'duracion_dias']

class RecetaMedicaSerializer(serializers.ModelSerializer):
    items = RecetaItemSerializer(many=True, read_only=True)
    class Meta:
        model = RecetaMedica
        fields = ['id', 'consulta', 'indicaciones', 'items']

class CitaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.ReadOnlyField(source='paciente.nombre')
    medico_nombre = serializers.ReadOnlyField(source='medico.nombre')
    class Meta:
        model = Cita
        fields = ['id', 'paciente', 'paciente_nombre', 'medico', 'medico_nombre', 'fecha_hora', 'estado', 'consulta']
