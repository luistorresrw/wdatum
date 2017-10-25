# -*-coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from principal.forms import NacionalidadForm, NivelInstruccionForm, RegimenTenenciaForm, AnioConstruccionForm, MaterialEstructuraForm, TipoProduccionForm
from .models import Nacionalidad, NivelInstruccion, RegimenTenencia, AnioConstruccion, MaterialEstructura, TipoProduccion


def index(request):
    mensaje = "index.html"

    context = {'mensaje': mensaje

    }
    return render(request, 'index.html', context)


# ---------------Nacionalidad---------------------#


def crear_nacionalidad(request):
    lista = Nacionalidad.objects.all()
    if request.method == 'POST':
        form = NacionalidadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NacionalidadForm()

    context = {'lista': lista, 'form': form, }
    return render(request, 'crear_nacionalidad.html', context)


def editar_nacionalidad(request, id):
    form = NacionalidadForm()
    nacionalidad = get_object_or_404(Nacionalidad, id=id)
    lista = Nacionalidad.objects.all()

    if request.method == 'POST':
        form = NacionalidadForm(request.POST, instance=nacionalidad)
        if form.is_valid():
            nacionalidad = form.save(commit=False)
            nacionalidad.save()
            return redirect('crear_nacionalidad')
        else:
            form = NacionalidadForm(instance=nacionalidad)
    context = {'lista': lista, 'form': form, }
    return render(request, './editar_nacionalidad.html', context)


def borrar_nacionalidad(request, id):
    nacionalidad = get_object_or_404(Nacionalidad, id=id)
    nacionalidad.delete()
    return redirect('crear_nacionalidad')


# ------------Nivel de Instruccion-------------------


def crear_nivel_instruccion(request):
    lista = NivelInstruccion.objects.all()
    if request.method == 'POST':
        form = NivelInstruccionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NivelInstruccionForm()

    context = {'lista': lista, 'form': form, }
    return render(request, 'crear_nivel_instruccion.html', context)


def editar_nivel_instruccion(request, id):
    form = NivelInstruccionForm()
    nivel_instruccion = get_object_or_404(NivelInstruccion, id=id)
    lista = NivelInstruccion.objects.all()

    if request.method == 'POST':
        form = NacionalidadForm(request.POST, instance=nivel_instruccion)
        if form.is_valid():
            nivel_instruccion = form.save(commit=False)
            nivel_instruccion.save()
            return redirect('crear_nivel_instruccion')
        else:
            form = NivelInstruccionForm(instance=nivel_instruccion)
    context = {'lista': lista, 'form': form, }
    return render(request, './editar_nivel_instruccion.html', context)


def borrar_nivel_instruccion(request, id):
    nivel_instruccion = get_object_or_404(NivelInstruccion, id=id)
    nivel_instruccion.delete()
    return redirect('crear_nivel_instruccion')


# ------------Regimen de Tenencia-------------------


def crear_regimen_tenencia(request):
    lista = RegimenTenencia.objects.all()
    if request.method == 'POST':
        form = RegimenTenenciaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegimenTenenciaForm()

    context = {'lista': lista, 'form': form, }
    return render(request, 'crear_regimen_tenencia.html', context)


def editar_regimen_tenencia(request, id):
    form = RegimenTenenciaForm()
    regimen_tenencia = get_object_or_404(RegimenTenencia, id=id)
    lista = RegimenTenencia.objects.all()

    if request.method == 'POST':
        form = RegimenTenenciaForm(request.POST, instance=regimen_tenencia)
        if form.is_valid():
            regimen_tenencia = form.save(commit=False)
            regimen_tenencia.save()
            return redirect('crear_regimen_tenencia')
        else:
            form = RegimenTenenciaForm(instance=regimen_tenencia)
    context = {

        'lista': lista,
        'form': form,
    }
    return render(request,'./editar_regimen_tenencia.html', context)


def borrar_regimen_tenencia(request, id):
    regimen_tenencia = get_object_or_404(RegimenTenencia, id=id)
    regimen_tenencia.delete()
    return redirect('crear_regimen_tenencia')


# ------------Año de construcción----------------------


def crear_anio_construccion(request):
    lista = AnioConstruccion.objects.all()
    if request.method == 'POST':
        form = AnioConstruccionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegimenTenenciaForm()

    context = {'lista': lista, 'form': form }
    return render(request, 'crear_anio_construccion.html', context)


def editar_anio_construccion(request, id):
    form = AnioConstruccionForm()
    anio_construccion = get_object_or_404(AnioConstruccion, id=id)
    lista = AnioConstruccion.objects.all()

    if request.method == 'POST':
        form = AnioConstruccionForm(request.POST, instance=anio_construccion)
        if form.is_valid():
            anio_construccion= form.save(commit=False)
            anio_construccion.save()
            return redirect('crear_anio_construccion')
        else:
            form = AnioConstruccionForm(instance=anio_construccion)
    context = {'lista': lista,'form': form,}
    return render(request,'./editar_anio_construccion.html', context)


def borrar_anio_construccion(request, id):
    anio_construccion = get_object_or_404(AnioConstruccion, id=id)
    anio_construccion.delete()
    return redirect('crear_anio_construccion')


# -----------Material Estructura-----------------------

def crear_material_estructura(request):
    lista = MaterialEstructura.objects.all()
    if request.method == 'POST':
        form = MaterialEstructuraForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MaterialEstructuraForm()

    context = {'lista': lista, 'form': form}
    return render(request, 'crear_material_estructura.html', context)


def editar_material_estructura(request, id):
    form = MaterialEstructuraForm()
    material_estructura = get_object_or_404(MaterialEstructura, id=id)
    lista = MaterialEstructura.objects.all()

    if request.method == 'POST':
        form = MaterialEstructuraForm(request.POST, instance=material_estructura)
        if form.is_valid():
            material_estructura = form.save(commit=False)
            material_estructura.save()
            return redirect('crear_material_estructura')
        else:
            form = MaterialEstructuraForm(instance=material_estructura)
    context = {'lista': lista, 'form':form}
    return render(request, './editar_material_estructura.html', context)


def borrar_material_estructura(request, id):
    material_estructura = get_object_or_404(MaterialEstructura, id=id)
    material_estructura.delete()
    return redirect('crear_material_estructura')


# -----------Tipo de Producción -----------------------

def crear_tipo_produccion(request):
    lista = TipoProduccion.objects.all()
    if request.method == 'POST':
        form = TipoProduccionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TipoProduccionForm()

    context = {'lista': lista, 'form': form}
    return render(request, 'crear_tipo_produccion.html', context)


def editar_tipo_produccion(request, id):
    form = TipoProduccionForm()
    tipo_produccion = get_object_or_404(TipoProduccion, id=id)
    lista = TipoProduccion.objects.all()

    if request.method == 'POST':
        form = TipoProduccionForm(request.POST, instance=tipo_produccion)
        if form.is_valid():
            tipo_produccion = form.save(commit=False)
            tipo_produccion.save()
            return redirect('crear_tipo_produccion')
        else:
            form = TipoProduccionForm(instance=tipo_produccion)
    context = {'lista': lista, 'form':form}
    return render(request, './editar_tipo_produccion.html', context)


def borrar_tipo_produccion(request, id):
    tipo_produccion = get_object_or_404(TipoProduccion, id=id)
    tipo_produccion.delete()
    return redirect('crear_tipo_produccion')
