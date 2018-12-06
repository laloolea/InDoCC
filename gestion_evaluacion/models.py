from django.db import models
# Create your models here.

class Evaluacion(models.Model):
    Hay_evaluacion_estudiantes = models.BooleanField(default=False)
    Descripcion_evaluacion_estudiantes = models.TextField(default="", blank=True, null=True)
    Hay_mecanismos_evaluacion = models.BooleanField(default=False)
    Esta_reglamentado_mecanismos = models.BooleanField(default=False)
    Descripcion_mecanismos = models.TextField(default="", blank=True, null=True)
    Grupo_colegiado = models.BooleanField(default=False)
    Descripcion_gruposColegiados = models.TextField(default="", blank=True, null=True)
    Estudiantes = models.BooleanField(default=False)
    Descripcion_estudiantes = models.TextField(default="", blank=True, null=True)
    Otras_instancias = models.BooleanField(default=False)
    Descripcion_instancias = models.TextField(default="", blank=True, null=True)
    Hay_difusion = models.BooleanField(default=False)
    Tipo_difusion = models.TextField(default="", blank=True, null=True)
    Descripcion_entrega = models.TextField(default="", blank=True, null=True)
    Hay_criterios = models.BooleanField(default=False)
    Criterios_principales = models.TextField(default="", blank=True, null=True)
    Hay_programa_estimulos = models.BooleanField(default=False)
    DescripcionDifusion = models.TextField(default="", blank=True, null=True)
