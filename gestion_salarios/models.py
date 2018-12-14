from django.db import models

# Create your models here.
class Salarios(models.Model):
    Contrato_colectivo = models.FileField(upload_to="evidencias/",null=True,blank=True)



