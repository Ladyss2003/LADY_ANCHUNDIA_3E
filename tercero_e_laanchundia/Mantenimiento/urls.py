from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicioDef, name='inicio'),
    path('crearTelefono/', views.crearTelefonoDef, name='crear'),
    path('registrarTelefono/', views.registrarTelefonoDef, name='registrarTelefono'),
    path('editarTelefono/<int:id>', views.editarTelefonoDef, name='editarTelefono'),
    path('edicionTelefono/', views.edicionTelefonoDef, name='edicionTelefono'),
    path('borrarTelefono/<id>', views.borraTelefonoDef, name='borrarTelefono'),
    path('buscar_telefono/', views.buscar_telefonos, name='buscartelefono'),

]