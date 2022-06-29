from django.urls import path
from Appsecurity import views

urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('alarmas', views.alarmas, name="Alarmas"),
    path('cercos', views.Cercos, name="Cercos"),
    path('camaras', views.camaras, name="Camaras"),
    path('formulario', views.crearAlarma, name="Formulario"),
    path('formulario_camara', views.crearCamara, name="FormularioCamaras"),
    path('formulario_cerco', views.crearCerco, name="FormularioCercos"),
    path('buscarAlarma', views.buscarAlarma, name="BuscarAlarma"),
    path('buscar/', views.buscar)

]
