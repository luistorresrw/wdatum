#-*-coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from principal.forms import NacionalidadForm, NivelInstruccionForm
from .models import Nacionalidad, NivelInstruccion

def index(request):

	mensaje = "index.html"

	context = {
		'mensaje':mensaje

	}
	return render(request, 'index.html', context)

#----------------nacionalidad---------------------
def crear_nacionalidad(request):
	lista = Nacionalidad.objects.all()
	if request.method == 'POST':
		form = NacionalidadForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = NacionalidadForm()

	context = {
		'lista':lista,
		'form':form,
	}
	return render(request, 'crear_nacionalidad.html', context)

def editar_nacionalidad(request, id):
	form = NacionalidadForm()
	nacionalidad = get_object_or_404(Nacionalidad, id = id)
	lista = Nacionalidad.objects.all()

	if request.method == 'POST':	
		form = NacionalidadForm(request.POST, instance = nacionalidad)
		if form.is_valid():
			nacionalidad = form.save(commit = False)
			nacionalidad.save()
			return redirect('crear_nacionalidad')
		else:
			form = NacionalidadForm(instance = nacionalidad)
	context = {
		'lista':lista,
		'form':form,
	}
	return render(request, './editar_nacionalidad.html', context)
	
def borrar_nacionalidad(request, id):
	nacionalidad = get_object_or_404(Nacionalidad, id = id)
	nacionalidad.delete()
	return redirect('crear_nacionalidad')

#------------nivel de instruccion-------------------
def crear_nivel_instruccion(request):
	lista = NivelInstruccion.objects.all()
	if request.method == 'POST':
		form = NivelInstruccionForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = NivelInstruccionForm()

	context = {
		'lista':lista,
		'form':form,
	}
	return render(request, 'crear_nivel_instruccion.html', context)

def editar_nivel_instruccion(request, id):
	form = NivelInstruccionForm()
	nivel_instruccion = get_object_or_404(NivelInstruccion, id = id)
	lista = NivelInstruccion.objects.all()

	if request.method == 'POST':	
		form = NacionalidadForm(request.POST, instance = nivel_instruccion)
		if form.is_valid():
			nivel_instruccion = form.save(commit = False)
			nivel_instruccion.save()
			return redirect('crear_nivel_instruccion')
		else:
			form = NivelInstruccionForm(instance = nivel_instruccion)
	context = {
		'lista':lista,
		'form':form,
	}
	return render(request, './editar_nivel_instruccion.html', context)
	

def borrar_nivel_instruccion(request, id):
	nivel_instruccion = get_object_or_404(NivelInstruccion, id = id)
	nivel_instruccion.delete()
	return redirect('crear_nivel_instruccion')

