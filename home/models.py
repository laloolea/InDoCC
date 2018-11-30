from django.db import models

class Pregunta(models.Model):
    nombre = models.CharField(max_length=10)
    pregunta = models.CharField(max_length=255)
    descripcion = models.TextField()
    #archivo_evidencia = models.ForeignKey(...)
    #tabla_evidencia = models.ForeignKey(...)

    def __str__(self):
        return self.nombre

class PreguntaCerrada(Pregunta):
    respuesta = models.BooleanField(default=False)

class PreguntaMultiple(Pregunta):
    respuesta = models.TextField()
