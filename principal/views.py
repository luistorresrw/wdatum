# -*-coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from principal.forms import NacionalidadForm, NivelInstruccionForm, RegimenTenenciaForm, AnioConstruccionForm, MaterialEstructuraForm, TipoProduccionForm, EleccionCultivoForm, TipoCultivoForm, EspecieForm, FactorClimaticoForm, TripleLavadoForm, AsesoramientoForm
from .models import Nacionalidad, NivelInstruccion, RegimenTenencia, AnioConstruccion, MaterialEstructura, TipoProduccion, EleccionCultivo, TipoCultivo, Especie, FactorClimatico, TripleLavado, Asesoramiento


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


# -----------Eleccion de Cultivo ------------------------

def crear_eleccion_cultivo(request):
    lista = EleccionCultivo.objects.all()
    if request.method == 'POST':
        form = EleccionCultivoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EleccionCultivoForm()

    context = {'lista': lista, 'form': form}
    return render(request, 'crear_eleccion_cultivo.html', context)


def editar_eleccion_cultivo(request, id):
    form = EleccionCultivoForm()
    eleccion_cultivo = get_object_or_404(EleccionCultivo, id=id)
    lista = EleccionCultivo.objects.all()

    if request.method == 'POST':
        form = EleccionCultivoForm(request.POST, instance=eleccion_cultivo)
        if form.is_valid():
            eleccion_cultivo = form.save(commit=False)
            eleccion_cultivo.save()
            return redirect('crear_eleccion_cultivo')
        else:
            form = EleccionCultivoForm(instance=eleccion_cultivo)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_eleccion_cultivo.html', context)


def borrar_eleccion_cultivo(request, id):
    eleccion_cultivo = get_object_or_404(EleccionCultivo, id=id)
    eleccion_cultivo.delete()
    return redirect('crear_eleccion_cultivo')


# -----------Tipo de Cultivo ------------------------


def crear_tipo_cultivo(request):
    lista = TipoCultivo.objects.all()
    if request.method == 'POST':
        form = TipoCultivoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TipoCultivoForm()

    context = {'lista': lista, 'form': form}
    return render(request, 'crear_tipo_cultivo.html', context)


def editar_tipo_cultivo(request, id):
    form = TipoCultivoForm()
    tipo_cultivo = get_object_or_404(TipoCultivo, id=id)
    lista = TipoCultivo.objects.all()

    if request.method == 'POST':
        form = TipoCultivoForm(request.POST, instance=tipo_cultivo)
        if form.is_valid():
            tipo_cultivo = form.save(commit=False)
            tipo_cultivo.save()
            return redirect('crear_tipo_cultivo')
        else:
            form = TipoCultivoForm(instance=tipo_cultivo)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_tipo_cultivo.html', context)


def borrar_tipo_cultivo(request, id):
    tipo_cultivo = get_object_or_404(TipoCultivo, id=id)
    tipo_cultivo.delete()
    return redirect('crear_tipo_cultivo')


# ------------------Especie ----------------------------


def crear_especie(request):
    lista = Especie.objects.all()
    if request.method == 'POST':
        form = EspecieForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EspecieForm()

    context = {'lista': lista, 'form': form}
    return render(request, 'crear_especie.html', context)


def editar_especie(request, id):
    form = EspecieForm()
    especie = get_object_or_404(Especie, id=id)
    lista = Especie.objects.all()

    if request.method == 'POST':
        form = EspecieForm(request.POST, instance=especie)
        if form.is_valid():
            especie = form.save(commit=False)
            especie.save()
            return redirect('crear_especie')
        else:
            form = EspecieForm(instance=especie)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_especie.html', context)


def borrar_especie(request, id):
    especie = get_object_or_404(Especie, id=id)
    especie.delete()
    return redirect('crear_especie')


# ----------------Factor Climático-----------------------


def crear_factor_climatico(request):
    lista = FactorClimatico.objects.all()
    if request.method == 'POST':
        form = FactorClimaticoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FactorClimaticoForm()

    context = {'lista': lista, 'form': form}
    return render(request, 'crear_factor_climatico.html', context)


def editar_factor_climatico(request, id):
    form = FactorClimaticoForm()
    factor_climatico = get_object_or_404(FactorClimatico, id=id)
    lista = FactorClimatico.objects.all()

    if request.method == 'POST':
        form = FactorClimaticoForm(request.POST, instance=factor_climatico)
        if form.is_valid():
            factor_climatico = form.save(commit=False)
            factor_climatico.save()
            return redirect('crear_factor_climatico')
        else:
            form = EspecieForm(instance=factor_climatico)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_factor_climatico.html', context)


def borrar_factor_climatico(request, id):
    factor_climatico= get_object_or_404(FactorClimatico, id=id)
    factor_climatico.delete()
    return redirect('crear_factor_climatico')


# ----------------Triple Lavado-----------------------


def crear_triple_lavado(request):
    lista = TripleLavado.objects.all()
    if request.method == 'POST':
        form = TripleLavadoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TripleLavadoForm()

    context = {'lista': lista, 'form': form}
    return render(request, 'crear_triple_lavado.html', context)


def editar_triple_lavado(request, id):
    form = TripleLavadoForm()
    triple_lavado = get_object_or_404(TripleLavado, id=id)
    lista = TripleLavado.objects.all()

    if request.method == 'POST':
        form = TripleLavadoForm(request.POST, instance=triple_lavado)
        if form.is_valid():
            triple_lavado = form.save(commit=False)
            triple_lavado.save()
            return redirect('crear_triple_lavado')
        else:
            form = TripleLavadoForm(instance=triple_lavado)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_triple_lavado.html', context)


def borrar_triple_lavado(request, id):
    triple_lavado= get_object_or_404(TripleLavado, id=id)
    triple_lavado.delete()
    return redirect('crear_triple_lavado')


# ----------------Asesoramiento-----------------------


def crear_asesoramiento(request):
    lista = Asesoramiento.objects.all()
    if request.method == 'POST':
        form = AsesoramientoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AsesoramientoForm()

    context = {'lista': lista, 'form': form}
    return render(request, 'crear_asesoramiento.html', context)


def editar_asesoramiento(request, id):
    form = AsesoramientoForm()
    asesoramiento = get_object_or_404(Asesoramiento, id=id)
    lista = Asesoramiento.objects.all()

    if request.method == 'POST':
        form = AsesoramientoForm(request.POST, instance=asesoramiento)
        if form.is_valid():
            asesoramiento = form.save(commit=False)
            asesoramiento.save()
            return redirect('crear_asesoramiento')
        else:
            form = AsesoramientoForm(instance=asesoramiento)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_asesoramiento.html', context)


def borrar_asesoramiento(request, id):
    asesoramiento = get_object_or_404(Asesoramiento, id=id)
    asesoramiento.delete()
    return redirect('crear_asesoramiento')