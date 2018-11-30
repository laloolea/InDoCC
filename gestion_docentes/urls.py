from django.urls import path

from . import views

app_name = 'gestion_docentes'
urlpatterns = [
    path('', views.index, name="index"),
    path('registro/', views.registro, name="registro"),
    path('usuario/<str:user>', views.detail, name="detail"),
]