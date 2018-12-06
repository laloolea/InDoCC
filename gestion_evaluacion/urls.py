from django.urls import path
from gestion_evaluacion.views import EvaluacionAdd , EvaluacionViewUpdate , EvaluacionClean

urlpatterns = [
    path('Agregar',EvaluacionAdd.as_view() , name="Agregar"),
    path('VerEditar', EvaluacionViewUpdate.as_view(), name='VerEditar'),
    path('Eliminar', EvaluacionClean.as_view(), name='Eliminar'),
]

