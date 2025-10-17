"""
Bloque de Modelos: Entidades y relaciones para Salud Vital Ltda.
Incluye CHOICES (mejora 1) y nueva tabla adicional (mejora 2: RecetaItem).
"""
from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    RUT = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo_choices = [  # CHOICES de ejemplo
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    sexo = models.CharField(max_length=1, choices=sexo_choices)

    def __str__(self):
        return f"{self.nombre} ({self.RUT})"

class Medico(models.Model):
    RUT = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, related_name='medicos')

    def __str__(self):
        return f"Dr(a). {self.nombre} - {self.especialidad.nombre}"

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class ConsultaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='consultas')
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length=200)
    diagnostico = models.TextField(blank=True)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Consulta de {self.paciente} con {self.medico} el {self.fecha:%Y-%m-%d}"

class RecetaMedica(models.Model):
    consulta = models.OneToOneField(ConsultaMedica, on_delete=models.CASCADE, related_name='receta')
    indicaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Receta consulta #{self.consulta_id}"

class RecetaItem(models.Model):  # Tabla adicional para ítems de receta (mejora 2)
    receta = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE, related_name='items')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    duracion_dias = models.PositiveIntegerField(default=7)

    def __str__(self):
        return f"{self.medicamento} - {self.dosis}, {self.frecuencia} x {self.duracion_dias}d"

class Cita(models.Model):
    """
    Segmento 8: Cita (agenda de atenciones) enlazada con Paciente y Médico.
    - Coherente con el dominio: una Cita puede anteceder a una ConsultaMedica.
    - Incluye CHOICES para el estado.
    """
    ESTADO_CHOICES = [
        ('programada', 'Programada'),
        ('atendida', 'Atendida'),
        ('cancelada', 'Cancelada'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='citas')
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='programada')
    consulta = models.OneToOneField(ConsultaMedica, on_delete=models.SET_NULL, null=True, blank=True, related_name='cita')

    def __str__(self):
        return f"Cita {self.fecha_hora:%Y-%m-%d %H:%M} - {self.paciente} / {self.medico} ({self.estado})"
