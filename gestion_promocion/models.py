from django.db import models

# Create your models here.

class Promocion(models.Model):
    Hay_proceso_promocion = models.BooleanField(default=False)
    Hay_reglamento_proceso = models.BooleanField(default=False)
    Descripcion = models.TextField(default="", blank=True, null=True)
    Hay_difusion_proceso = models.BooleanField(default=False)
    DescripcionDifusion = models.TextField(default="", blank=True, null=True)