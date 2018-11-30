from django.urls import path

from . import views

app_name = 'gestion_promocion'
urlpatterns = [
    path('', views.promocion, name="promocion"),

    path('/editarPromocion', views.promocion_form, name="promocionForm"),

]

