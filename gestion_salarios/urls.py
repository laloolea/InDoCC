from django.urls import path
from gestion_salarios.views import SalariosAdd , SalariosViewUpdate , SalariosClean

urlpatterns = [
    path('Agregar',SalariosAdd.as_view() , name="Agregar"),
    path('VerEditar', SalariosViewUpdate.as_view(), name='VerEditar'),
    path('Eliminar', SalariosClean.as_view(), name='Eliminar'),
]

