from django.urls import path
from gestion_promocion.views import PromocionAdd, PromocionViewUpdate , PromocionClean

urlpatterns = [
    path('Agregar',PromocionAdd.as_view() , name="Agregar"),
    path('VerEditar', PromocionViewUpdate.as_view(), name='VerEditar'),
    path('Eliminar', PromocionClean.as_view(), name='Eliminar'),
]

