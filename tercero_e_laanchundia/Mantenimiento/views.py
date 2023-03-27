from django.shortcuts import render, redirect
from .models import Telefonos, Marcas
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def buscar_telefonos(request):
    query = request.GET.get('q')
    telefono = Telefonos.objects.filter(
        Q(modelo__icontains=query) |
        Q(descripcion__icontains=query) |
        Q(precio__icontains=query) |
        Q(marca__nombre__contains=query) |
        Q(disponibilidad__icontains=query)
    )
    return render(request, 'InicioTelefonos.html', {'telefono': telefono})

def inicioDef(request):
    telefono = Telefonos.objects.all()
    return render(request, 'InicioTelefonos.html', {'telefono': telefono})

def crearTelefonoDef(request):
    marca = Marcas.objects.all()
    return render(request, 'GestionarTelefonos.html', {'marca': marca})

def registrarTelefonoDef(request):
    id = request.POST['txtId']
    modelo = request.POST['txtModelo']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    marca_id = request.POST['txtMarca']
    marca = Marcas.objects.get(id=marca_id)
    disponibilidad = request.POST['txtDisponibilidad']

    try:
        telefono = Telefonos.objects.create(
            id=id, modelo=modelo,
            descripcion=descripcion,
            precio=precio,
            disponibilidad=disponibilidad,
            marca=marca)
        messages.success(request, 'Telefono Añadido Correctamente.')
        return render(request, 'GestionarTelefonos.html', {'mensaje_tipo': 'success', 'mensaje_texto': 'Telefono Añadido Correctamente.'})

    except:
        messages.error(request, 'Ocurrió un error durante el registro. Por favor revise, inténtelo de nuevo.')
        return render(request, 'GestionarTelefonos.html', {'mensaje_tipo': 'error', 'mensaje_texto': 'Ocurrió un error durante el registro. Por favor revise, inténtelo de nuevo.'})

def editarTelefonoDef(request, id):
    telefono = Telefonos.objects.get(id=id)
    marca = Marcas.objects.all()
    return render(request, 'EditarTelefonos.html', {'telefono': telefono, 'marca': marca})

def edicionTelefonoDef(request):
    id = request.POST['txtId']
    modelo = request.POST['txtModelo']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    disponibilidad = request.POST['txtDisponibilidad']

    telefono = Telefonos.objects.get(id=id)
    telefono.modelo = modelo
    telefono.descripcion = descripcion
    telefono.precio = precio
    telefono.disponibilidad = disponibilidad
    telefono.save()


    return redirect('inicio')

def borraTelefonoDef(request, id):
    telefono = Telefonos.objects.get(id=id)
    telefono.delete()
    return redirect('inicio')