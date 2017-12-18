# -*-coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from principal.forms import *
from .models import *
from datetime import date,datetime
import xlwt

from django.apps import apps

def exportar_xls(request):
    """Definicion que permite exportar los datos minimos de las encuestas
       en una hoja de calculo tipo excel."""

    #define el tipo de respuesta a ms-excel
    response = HttpResponse(content_type='application/ms-excel')
    #Establece el nombre del archivo que se genera
    response['Content-Disposition'] = 'attachment; filename="Encuestas.xls"'

    #Crea un libro de trabajo
    wb = xlwt.Workbook(encoding='utf-8')
    #Crea una nueva hoja dentro del libro y le establece el nombre
    ws = wb.add_sheet('Encuestas')

    #Crea un puntero a la primer fila dentro de la hoja
    row_num = 0


    #Define un estilo de fuente
    font_style = xlwt.XFStyle()
    #Establece el estilo Negrita
    font_style.font.bold = True

    #Define el nombre de las columnas dentro de la hoja
    columns = ['Fecha', 'Nombre establecimiento', 'Regimen de tenencia', 'Nombre Encuestado',
               'Apellido Encuestado' 'Edad', 'Nacionalidad', 'Instruccion','Cultivos',
               'Usa agroquimicos', 'Asesoramiento', 'Triple lavado', 'Agroquimicos usados', 'Plagas']

    #recorre el arreglo de
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    encuestas = Encuesta.objects.all()



    for encuesta in encuestas:

        row_num += 1
        row=[]
        row.append(encuesta.fecha.strftime('%d/%m/%Y'))
        row.append(encuesta.establecimiento.nombre)
        row.append(encuesta.establecimiento.regimenTenencia.descripcion)
        row.append(encuesta.encuestado.nombre)
        row.append(encuesta.encuestado.apellido)
        row.append(encuesta.encuestado.nacionalidad.descripcion)
        row.append(encuesta.encuestado.nivelInstruccion.descripcion)


        row.append(query_to_str(Cultivo.objects.filter(encuesta=encuesta),True))

        row.append("Si" if encuesta.agroquimico and encuesta.agroquimico.usa else "No")
        row.append(encuesta.agroquimico.asesoramiento.descripcion if encuesta.agroquimico else "")
        row.append(encuesta.agroquimico.tripleLavado.descripcion if encuesta.agroquimico else "")


        row.append(query_to_str(AgroquimicoUsado.objects.filter(encuesta=encuesta).values_list('producto',flat=True),False))


        row.append(query_to_str(AgroquimicoUsado.objects.filter(encuesta=encuesta).values_list('plaga',flat=True),False))

        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def query_to_str(queryset,especie):
    str_retorno = ""
    if especie:
        for element in queryset:
            str_retorno += element.especie.descripcion + " "
    else:
        for element in queryset:
            str_retorno += element + " "

    return str_retorno



def login(request):
    request.session.flush()
    if request.user.is_authenticated():  # si el usuario esta autenticado redirecciona a la pagina principal
        return HttpResponseRedirect(reverse('principal'))
    form = LoginForm()  # declaramos una variable que reciba los campos del formulario
    mensaje = ''  # declaramos una variable con un mensaje vacio
    user = None  # declaro la variable user a None

    if request.method == 'POST':  # validamos que los datos vengan por Post
        form = LoginForm(request.POST)# le pasamos el request a loginForm
        if form.is_valid():  # verificamos que el formato de los datos sea correcto
            usuario = form.data['user']  # asignamos a los datos de usuario a una variable usuario
            password = form.cleaned_data['password']  # asignamos a los datos de password a una variable password
            user = authenticate(username = usuario, password = password)  # valida que usuario y contraseña sean correctos
            if user is not None:
                request.session['user'] = usuario
                request.session['password'] = password
                auth_login(request, user)
                return HttpResponseRedirect('principal')
            else:
                mensaje = 'Usuario y/o password incorrecto, verifíquelo e inténtelo nuevamente.'
        else:
            mensaje = 'Debe completar ambos campos.'  # mandamos un mensaje de error
    context = {
        'form' : form,
        'mensaje' : mensaje,
    }
    return render(request, 'login.html', context)

@login_required
def logout(request):
    auth_logout(request)  # cierra sesion
    request.session.flush()
    return redirect(reverse('login'))  # redirecciona a login





@login_required
def lista_encuestas(request):
    lista = Encuesta.objects.all()
    context = {'lista':lista}
    return render(request, 'lista_encuestas.html', context )





@login_required
def cambiar_password(request):
    form = CambiarPasswordForm()
    mensaje = ""
    if request.method == 'POST':
        form = CambiarPasswordForm(request.POST)
        if form.is_valid():
            usuario = request.user
            password = form.data['password_actual']
            user = authenticate(username=usuario, password=password)
            if user is not None:
                nuevo_password = form.cleaned_data['nuevo_password']
                confirmar_password = form.cleaned_data['confirmar_password']
                if nuevo_password == confirmar_password:
                    user.set_password(nuevo_password)
                    try:
                        user.save()
                    except Exception as e:
                        raise e
                    logout(request)
                    return redirect(reverse('login'))
                else:
                    mensaje = "Los password no coinciden."
            else:
                mensaje = "Password actual no coincide con el usuario logueado."
        else:
            mensaje = "Debe completar todos los campos."
    context = {
        'mensaje':mensaje,
        'form':form
        }
    return render(request, 'cambiar_password.html', context)


def recuperar_password(request):
    form = RecuperarPasswordForm()
    mensaje =''
    usuario = Usuario()
    if request.method == 'POST':
        form = RecuperarPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email_user']
            usuario = Usuario.objects.get(username=email)
            if usuario:
                password = Usuario.objects.make_random_password(length=8)
                usuario.set_password(password)
                usuario.save()
                enviar_mail("Hola %s %s: <br> Bienvenido al Sistema de Administración de Encuestas Agropecuarias. "
                        "<br> Sus nuevas credenciales de acceso son las siguientes:<br> <b>Usuario: %s. <br> Password: %s."
                        "</b><br>Para su seguridad recuerde cambiar la contraseña asignada por una de su preferencia."%
                        (usuario.first_name, usuario.last_name, usuario.username,password),
                        usuario.username, 'Recuperación de password.')
                return HttpResponseRedirect("/")
            else:
                mensaje = 'La direccion de email ingresada no es válida.'
        else:
            mensaje = 'Es obligatorio ingresar una dirección de email válida.'
    context = {
        'form':form,
        'mensaje':mensaje,
    }
    return render(request, 'recuperar_password.html', context)

@login_required
def principal(request):
    lista = Establecimiento.objects.all()
    context = {
        'lista':lista,
    }
    return render(request, 'principal.html', context)

@login_required
def obtener_puntos(request):
    puntos = Establecimiento.objects.all()
    data = serializers.serialize("json",puntos)
    return HttpResponse(data,content_type="application/json")


# ---------------Usuarios---------------------#
@login_required
def crear_usuario(request):
    """MENSAJES AL USUARIO
    1 cuando el usuario que se intenta dar de alta existe
    2 cuando falla la creacion
    3 cuando no tiene el formato correcto
    4 cuando se creo con exito

    """
    mensaje = ""
    lista = Usuario.objects.all().order_by('-is_active')
    usuario = Usuario()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            password = Usuario.objects.make_random_password(length=8)
            usuario.username = form.cleaned_data['username']
            usuario.first_name = form.cleaned_data['first_name']
            usuario.last_name = form.cleaned_data['last_name']
            usuario.dni = form.cleaned_data['dni']
            usuario.rol = form.cleaned_data['rol']
            usuario.set_password(password)
            try:
                usuario.save()
                form = UsuarioForm(instance= usuario)
                enviar_mail("Hola %s %s: <br> Bienvenido al Sistema de Administración de Encuestas Agropecuarias. "
                        "<br> Sus credenciales de acceso son las siguientes:<br> <b>Usuario: %s. <br> Password: %s."
                        "</b><br>Para su seguridad recuerde cambiar la contraseña asignada por una de su preferencia."%
                        (usuario.first_name, usuario.last_name, usuario.username,password),
                        usuario.username,
                        'Alta de usuario.')
                form = UsuarioForm()
                messages.success(request, 'El usuario se creo correctamente.')
            except:
                messages.error(request, 'Error al crear usuario')
    else:
        form = UsuarioForm()

    context = {'lista':lista, 'form':form,'mensaje':mensaje}
    return render(request, 'crear_usuario.html', context)


def enviar_mail(mensaje,to,subject):
    html_content = (mensaje)
    from_email = 'm-datum UDC.'
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@login_required
def editar_usuario(request, id):
    form = UsuarioForm()
    usuario = get_object_or_404(Usuario, id=id)
    lista = Usuario.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario.username = form.cleaned_data['username']
            usuario.first_name = form.cleaned_data['first_name']
            usuario.last_name = form.cleaned_data['last_name']
            usuario.dni = form.cleaned_data['dni']
            usuario.rol = form.cleaned_data['rol']
            usuario.is_active = True
            usuario.save()
            messages.success(request, 'El usuario se editó correctamente.')
            return redirect('crear_usuario')
        else:
            messages.error(request, 'Error al editar usuario')
            form = UsuarioForm(instance=usuario)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)

    context = {
        'lista':lista,
        'form':form,
    }
    return render(request, 'editar_usuario.html', context)


@login_required
def borrar(request,modelo, id):
    objeto = get_object_or_404(apps.get_model(app_label='principal',model_name=modelo), id=id)
    objeto.is_active = False
    objeto.save()
    messages.success(request, 'El registro se eliminó correctamente.')
    retorno = 'crear_'+snake_caser(modelo)
    return redirect(retorno)

@login_required
def activar(request,modelo, id):
    usuario = get_object_or_404(apps.get_model(app_label='principal',model_name=modelo), id=id)
    usuario.is_active = True
    usuario.save()
    messages.success(request, 'El registro se activo correctamente.')
    retorno = 'crear_'+snake_caser(modelo)
    return redirect(retorno)


def snake_caser(string):
    snake = ''
    for index in range(len(string)):
        if index == 0:
            snake += string[index].lower()
        elif string[index].isupper():
            snake += '_'+string[index].lower()
        else:
            snake += string[index]
    return snake


# ---------------Nacionalidad---------------------#

@login_required
def crear_nacionalidad(request):
    lista = Nacionalidad.objects.all().order_by('-is_active')  # ordena el listado por es activo
    if request.method == 'POST':
        form = NacionalidadForm(request.POST)
        if form.is_valid():
            try:
                form.save()#guarda
                form = NacionalidadForm()  # crea un formulario vacio para que el template este limpio luego de crear un usuario
                messages.success(request, 'La nacionalidad se creó correctamente.')
            except:
                messages.error(request, 'Error al crear la nacionalidad.')

    else:
        form = NacionalidadForm()
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_nacionalidad.html', context)


@login_required
def editar_nacionalidad(request, id):
    form = NacionalidadForm()
    nacionalidad = get_object_or_404(Nacionalidad, id=id)
    lista = Nacionalidad.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = NacionalidadForm(request.POST, instance=nacionalidad)
        if form.is_valid():
            nacionalidad = form.save(commit=False)
            nacionalidad.save()
            messages.success(request, 'La nacionalidad se editó correctamente.')
            return redirect('crear_nacionalidad')
        else:
            messages.error(request, 'Error al editar nacionalidad')
            form = NacionalidadForm(instance=nacionalidad)
    if request.method == 'GET':
        form = NacionalidadForm(instance=nacionalidad)

    context = {
        'lista': lista,
        'form': form,
    }
    return render(request, './editar_nacionalidad.html', context)




# ------------Nivel de Instruccion-------------------
@login_required
def crear_nivel_instruccion(request):
    lista = NivelInstruccion.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = NivelInstruccionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = NivelInstruccionForm()
                messages.success(request, 'El nivel de instrucción se creó correctamente.')
            except:
                messages.error(request, 'Error al crear nivel de instrucción.')
    else:
        form = NivelInstruccionForm()
    context = {
        'lista': lista,
        'form': form,
    }
    return render(request, 'crear_nivel_instruccion.html', context)


@login_required
def editar_nivel_instruccion(request, id):
    form = NivelInstruccionForm()
    nivel_instruccion = get_object_or_404(NivelInstruccion, id=id)
    lista = NivelInstruccion.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = NivelInstruccionForm(request.POST, instance=nivel_instruccion)
        if form.is_valid():
            nivel_instruccion = form.save(commit=False)
            nivel_instruccion.save()
            messages.success(request, 'El nivel de instrucción se editó correctamente.')
            return redirect('crear_nivel_instruccion')
        else:
            messages.error(request, 'Error al editar el nivel de instrucción.')
            form = NivelInstruccionForm(instance=nivel_instruccion)
    if request.method == 'GET':
        form = NivelInstruccionForm(instance=nivel_instruccion)

    context = {
        'lista': lista,
        'form': form,
    }
    return render(request, './editar_nivel_instruccion.html', context)





# ------------Regimen de Tenencia-------------------

@login_required
def crear_regimen_tenencia(request):
    lista = RegimenTenencia.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = RegimenTenenciaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = RegimenTenenciaForm()
                messages.success(request, 'El regimen de tenencia se creó correctamente')
            except:
                messages.error(request, 'Error al crear regimen de tenencia.')
    else:
        form = RegimenTenenciaForm()
    context = {
        'lista': lista,
        'form': form,
    }
    return render(request, 'crear_regimen_tenencia.html', context)


@login_required
def editar_regimen_tenencia(request, id):
    form = RegimenTenenciaForm()
    regimen_tenencia = get_object_or_404(RegimenTenencia, id=id)
    lista = RegimenTenencia.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = RegimenTenenciaForm(request.POST, instance=regimen_tenencia)
        if form.is_valid():
            regimen_tenencia = form.save(commit=False)
            regimen_tenencia.save()
            messages.success(request, 'El regimen de tenencia se editó correctamente.')
            return redirect('crear_regimen_tenencia')
        else:
            messages.error(request, 'Error al editar el regimen de tenencia')
            form = RegimenTenenciaForm(instance=regimen_tenencia)
    if request.method == 'GET':
        form = RegimenTenenciaForm(instance=regimen_tenencia)
    context = {

        'lista': lista,
        'form': form,
    }
    return render(request,'./editar_regimen_tenencia.html', context)




# ------------Año de construcción----------------------

@login_required
def crear_anio_construccion(request):
    lista = AnioConstruccion.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = AnioConstruccionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = AnioConstruccionForm()
                messages.success(request, 'El año de construcción se creó correctamente.')
            except:
                messages.error(request, 'Error al crear año de construcción.')
    else:
        form = RegimenTenenciaForm()
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_anio_construccion.html', context)


@login_required
def editar_anio_construccion(request, id):
    form = AnioConstruccionForm()
    anio_construccion = get_object_or_404(AnioConstruccion, id=id)
    lista = AnioConstruccion.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = AnioConstruccionForm(request.POST, instance=anio_construccion)
        if form.is_valid():
            anio_construccion= form.save(commit=False)
            anio_construccion.save()
            messages.success(request, 'El año de construcción se editó correctamente')
            return redirect('crear_anio_construccion')
        else:
            messages.error(request, 'Error al editar el año de construcción.')
            form = AnioConstruccionForm(instance=anio_construccion)
    if request.method == 'GET':
        form = AnioConstruccionForm(instance=anio_construccion)
    context = {
        'lista': lista,
        'form': form,
    }
    return render(request, './editar_anio_construccion.html', context)





# -----------Material Estructura-----------------------

@login_required
def crear_material_estructura(request):
    lista = MaterialEstructura.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = MaterialEstructuraForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = MaterialEstructuraForm()
                messages.success(request, 'El material de estructura se creó correctamente.')
            except:
                messages.error(request, 'Error al crear material de estructura.')

    else:
        form = MaterialEstructuraForm()
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_material_estructura.html', context)


@login_required
def editar_material_estructura(request, id):
    form = MaterialEstructuraForm()
    material_estructura = get_object_or_404(MaterialEstructura, id=id)
    lista = MaterialEstructura.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = MaterialEstructuraForm(request.POST, instance=material_estructura)
        if form.is_valid():
            material_estructura = form.save(commit=False)
            material_estructura.save()
            messages.success(request, 'El material de estructura se editó correctamente')
            return redirect('crear_material_estructura')
        else:
            messages.error(request, 'Error al editar material de estructura')
            form = MaterialEstructuraForm(instance=material_estructura)
    if request.method == 'GET':
        form = MaterialEstructuraForm(instance=material_estructura)
    context = {'lista': lista, 'form':form}
    return render(request, './editar_material_estructura.html', context)




# -----------Tipo de Producción -----------------------
@login_required
def crear_tipo_produccion(request):
    lista = TipoProduccion.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = TipoProduccionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = TipoProduccionForm()
                messages.success(request, 'El tipo de producción se creo correctamente.')
            except:
                messages.error(request, 'Error al crear tipo de producción')
    else:
        form = TipoProduccionForm()
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_tipo_produccion.html', context)


@login_required
def editar_tipo_produccion(request, id):
    form = TipoProduccionForm()
    tipo_produccion = get_object_or_404(TipoProduccion, id=id)
    lista = TipoProduccion.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = TipoProduccionForm(request.POST, instance=tipo_produccion)
        if form.is_valid():
            tipo_produccion = form.save(commit=False)
            tipo_produccion.save()
            messages.success(request, 'El tipo de producción se editó correctamente.')
            return redirect('crear_tipo_produccion')
        else:
            messages.error(request, 'Error al editar el tipo de producción.')
            form = TipoProduccionForm(instance=tipo_produccion)
    if request.method == 'GET':
        form = TipoProduccionForm(instance=tipo_produccion)
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, './editar_tipo_produccion.html', context)





# -----------Eleccion de Cultivo ------------------------

@login_required
def crear_eleccion_cultivo(request):
    lista = EleccionCultivo.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = EleccionCultivoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = EleccionCultivoForm()
                messages.success(request, 'La elección de cultivo se creó correctamente.')
            except:
                messages.error(request, 'Error al crear elección de cultivo.')

    else:
        form = EleccionCultivoForm()

    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_eleccion_cultivo.html', context)


@login_required
def editar_eleccion_cultivo(request, id):
    form = EleccionCultivoForm()
    eleccion_cultivo = get_object_or_404(EleccionCultivo, id=id)
    lista = EleccionCultivo.objects.all()
    if request.method == 'POST':
        form = EleccionCultivoForm(request.POST, instance=eleccion_cultivo)
        if form.is_valid():
            eleccion_cultivo = form.save(commit=False)
            eleccion_cultivo.save()
            messages.success(request, 'La elección de cultivo se editó correctamente.')
            return redirect('crear_eleccion_cultivo')
        else:
            messages.error(request, 'Error al editar elección de cultivo.')
            form = EleccionCultivoForm(instance=eleccion_cultivo)
    if request.method == 'GET':
        form = EleccionCultivoForm(instance=eleccion_cultivo)
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, './editar_eleccion_cultivo.html', context)





# -----------Tipo de Cultivo ------------------------

@login_required
def crear_tipo_cultivo(request):
    lista = TipoCultivo.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = TipoCultivoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = TipoCultivoForm()
                messages.success(request, 'El tipo de cultivo se creó correctamente.')
            except:
                messages.error(request, 'Error al crear tipo de cultivo')
    else:
        form = TipoCultivoForm()
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_tipo_cultivo.html', context)


@login_required
def editar_tipo_cultivo(request, id):
    form = TipoCultivoForm()
    tipo_cultivo = get_object_or_404(TipoCultivo, id=id)
    lista = TipoCultivo.objects.all()
    if request.method == 'POST':
        form = TipoCultivoForm(request.POST, instance=tipo_cultivo)
        if form.is_valid():
            tipo_cultivo = form.save(commit=False)
            tipo_cultivo.save()
            messages.success(request, 'El tipo de cultivo se editó correctamente.')
            return redirect('crear_tipo_cultivo')
        else:
            messages.error(request, 'Error al editar tipo de cultivo.')
            form = TipoCultivoForm(instance=tipo_cultivo)
    if request.method == 'GET':
        form = TipoCultivoForm(instance=tipo_cultivo)
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, './editar_tipo_cultivo.html', context)




# ------------------Especie ----------------------------


@login_required
def crear_especie(request):
    lista = Especie.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = EspecieForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = EspecieForm()
                messages.success(request, 'La especie se creó correctamente.')
            except:
                messages.error(request, 'Error al crear la especie.')
    else:
        form = EspecieForm()
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_especie.html', context)


@login_required
def editar_especie(request, id):
    form = EspecieForm()
    especie = get_object_or_404(Especie, id=id)
    lista = Especie.objects.all()
    if request.method == 'POST':
        form = EspecieForm(request.POST, instance=especie)
        if form.is_valid():
            especie = form.save(commit=False)
            especie.save()
            messages.success(request, 'La especie se editó correctamente.')
            return redirect('crear_especie')
        else:
            messages.error(request, 'Error al editar la especie.')
            form = EspecieForm(instance=especie)
    if request.method == 'GET':
        form = EspecieForm(instance=especie)
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, './editar_especie.html', context)





# ----------------Factor Climático-----------------------
@login_required
def crear_factor_climatico(request):
    lista = FactorClimatico.objects.all()
    if request.method == 'POST':
        form = FactorClimaticoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = FactorClimaticoForm()
                messages.success(request, 'El factor climático se creó correctamente.')
            except:
                messages.error(request, 'Error al crear el factor climático.')
    else:
        form = FactorClimaticoForm()

    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_factor_climatico.html', context)


@login_required
def editar_factor_climatico(request, id):
    form = FactorClimaticoForm()
    factor_climatico = get_object_or_404(FactorClimatico, id=id)
    lista = FactorClimatico.objects.all()
    if request.method == 'POST':
        form = FactorClimaticoForm(request.POST, instance=factor_climatico)
        if form.is_valid():
            factor_climatico = form.save(commit=False)
            factor_climatico.save()
            messages.success(request, 'El factor climático se editó correctamente')
            return redirect('crear_factor_climatico')
        else:
            messages.error(request, 'Error al editar el factor climático')
            form = EspecieForm(instance=factor_climatico)
    if request.method == 'GET':
        form = EspecieForm(instance=factor_climatico)
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, './editar_factor_climatico.html', context)





# ----------------Triple Lavado-----------------------
@login_required
def crear_triple_lavado(request):
    lista = TripleLavado.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = TripleLavadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = TripleLavadoForm()
                messages.success(request, 'El triple lavado se creó correctamente.')
            except:
                messages.error(request, 'Error al crear el triple lavado.')
    else:
        form = TripleLavadoForm()
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_triple_lavado.html', context)


@login_required
def editar_triple_lavado(request, id):
    form = TripleLavadoForm()
    triple_lavado = get_object_or_404(TripleLavado, id=id)
    lista = TripleLavado.objects.all()
    if request.method == 'POST':
        form = TripleLavadoForm(request.POST, instance=triple_lavado)
        if form.is_valid():
            triple_lavado = form.save(commit=False)
            triple_lavado.save()
            messages.success(request, 'El triple lavado se editó correctamente.')
            return redirect('crear_triple_lavado')
        else:
            messages.error(request, 'Error al editar el triple lavado.')
            form = TripleLavadoForm(instance=triple_lavado)
    if request.method == 'GET':
        form = TripleLavadoForm(instance=triple_lavado)
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, './editar_triple_lavado.html', context)





# ----------------Asesoramiento-----------------------

@login_required
def crear_asesoramiento(request):
    lista = Asesoramiento.objects.all().order_by('-is_active')
    if request.method == 'POST':
        form = AsesoramientoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = AsesoramientoForm()
                messages.success(request, 'El asesoramiento se creó correctamente.')
            except:
                messages.error(request, 'Error al crear el asesoramiento.')
    else:
        form = AsesoramientoForm()

    context = {
        'lista': lista,
        'form': form
    }
    return render(request, 'crear_asesoramiento.html', context)


@login_required
def editar_asesoramiento(request, id):
    form = AsesoramientoForm()
    asesoramiento = get_object_or_404(Asesoramiento, id=id)
    lista = Asesoramiento.objects.all()
    if request.method == 'POST':
        form = AsesoramientoForm(request.POST, instance=asesoramiento)
        if form.is_valid():
            asesoramiento = form.save(commit=False)
            asesoramiento.save()
            messages.success(request, 'El asesoramiento se editó correctamente')
            return redirect('crear_asesoramiento')
        else:
            messages.error(request, 'Error al editar el asesoramiento.')
            form = AsesoramientoForm(instance=asesoramiento)
    if request.method == 'GET':
        form = AsesoramientoForm(instance=asesoramiento)
    context = {
        'lista': lista,
        'form': form
    }
    return render(request, './editar_asesoramiento.html', context)




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset            = User.objects.all().order_by('date_joined')
    serializer_class    = UserSerializer

class GroupviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset            = Group.objects.all()
    serializer_class    = GroupSerializer




class UpdateViewSet(viewsets.ModelViewSet):
    """
    API endpoint que gestiona todas las actualizaciones
    generadas en la base de datos de las LookUp tables
    """
    queryset = Updates.objects.all()
    serializer_class = UpdatesSerializer

@api_view(['GET'])
def UpdatesPosteriores(request,last_update):
    """
    API endpoint que Devuelve todas las actualizaciones posteriores
    a la recibida por parametro
    """
    updates = Updates.objects.filter(id__gt=last_update)

    if request.method == 'GET':
        serializer = UpdatesSerializer(updates,many=True)
        return Response(serializer.data)
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updates_from_mobile(request):
    """
    API endpoint que recibe las actualizaciones desde el movil
    """
    if request.method == 'POST':
        update = UpdatesFromMobileSerializer(data=request.data)
        if update.is_valid():
            update.save()
            return Response(update.data,status = status.HTTP_201_CREATED)
        return Response(update.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def lastUpdate(request):
    """
    Devuelve la ultima actualizacion disponible
    """
    update = Updates.objects.latest('id')
    if request.method == 'GET':
        serializer = UpdatesSerializer(update)
        return Response(serializer.data)
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT'])
def sincro_encuestado(request):
    """
    API endpoint que Lista todos los encuestados o Crea nuevos
    """
    if request.method == 'GET':
        encuestados = Encuestado.objects.all()
        serializer = EncuestadoSerializer(encuestados,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        encuestado = EncuestadoSerializer(data = request.data)
        if encuestado.is_valid():
            encuestado.save(creado = date.today())
            return Response(encuestado.data, status = status.HTTP_201_CREATED)
        return Response(encuestado.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT'])
def sincro_establecimiento(request):
    #  class EstablecimientoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que lista todos los establecimientos o crea nuevos
    """

    if request.method == "GET":
        establecimientos = Establecimiento.objects.all()
        serializer = EstablecimientoSerializer(establecimientos,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        establecimiento = EstablecimientoSerializer(data = request.data)
        if establecimiento.is_valid():
            establecimiento.save(creado = date.today())
            return Response(establecimiento.data,status= status.HTTP_201_CREATED)
        return Response(establecimiento.errors,status= status.HTTP_400_BAD_REQUEST)

class RegimenTenenciaViewSet(viewsets.ModelViewSet):

    queryset = RegimenTenencia.objects.all()
    serializer_class = RegimenTenenciaSerializer


@api_view(['GET','POST'])
def sincro_familia(request):
    """
    API endpoint que lista todos los registros de familia
    o crea un nuevo registro en la base de datos
    """
    if request.method == 'GET':
        familias = Familia.objects.all()
        serializer = FamiliaSerializer(familias,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        familia = FamiliaSerializer(data = request.data)
        if familia.is_valid():
            familia.save(creado = date.today())
            return Response(familia.data, status = status.HTTP_201_CREATED)
        return Response(familia.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT'])
def sincro_agroquimico(request):
    """
    API endpoint que lista todos los registros de agroquimicos
    o crea un nuevo registro en la base de datos
    """
    if request.method == 'GET':
        agroquimicos = Agroquimico.objects.all()
        serializer = AgroquimicoSerializer(agroquimicos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        agroquimico = AgroquimicoSerializer(data = request.data)
        if agroquimico.is_valid():
            agroquimico.save(creado = date.today())
            return Response(agroquimico.data, status = status.HTTP_201_CREATED)
        return Response(agroquimico.errors, status = status.HTTP_400_BAD_REQUEST)


class NacionalidadViewSet(viewsets.ModelViewSet):

    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer


class NivelInstruccionViewSet(viewsets.ModelViewSet):

    queryset = NivelInstruccion.objects.all()
    serializer_class = NivelInstruccionSerializer


class FactorClimaticoViewSet(viewsets.ModelViewSet):

    queryset = FactorClimatico.objects.all()
    serializer_class = FactorClimaticoSerializer


class TripleLavadoViewSet(viewsets.ModelViewSet):

    queryset = TripleLavado.objects.all()
    serializer_class = TripleLavadoSerializer


class AsesoramientoViewSet(viewsets.ModelViewSet):

    queryset = Asesoramiento.objects.all()
    serializer_class = AsesoramientoSerializer


@api_view(['GET','POST','PUT'])
def sincro_encuesta(request):
    """
    API Endpoint que permite listar todas las encuestas
    o crear nuevas encuestas
    """
    if request.method == 'GET':
        encuestas = Encuesta.objects.all()
        serializer = EncuestaSerializer(encuestas, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        encuesta = EncuestaSerializer(data = request.data)
        if encuesta.is_valid():
            #transaccion = encuesta.validated_data['transaccion']
            #encuestado = Encuestado.objects.get(transaccion = transaccion)
            #establecimiento = Establecimiento.objects.get(transaccion = transaccion)
            #agroquimico = Agroquimicos.objects.get(transaccion = transaccion)
            #familia = Familia.objects.get(transaccion = transaccion )

            encuesta.save(creado = date.today())
            return Response(encuesta.data, status = status.HTTP_201_CREATED)
        return Response(encuesta.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT'])
def sincro_invernaculo(request):
    """
    API Endpoint que permite listar todos los invernaculos
    o crear nuevos invernaculos
    """
    if request.method == 'GET':
        invernaculos = Invernaculo.objects.all()
        serializer = InvernaculoSerializer(invernaculos, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        invernaculo = InvernaculoSerializer(data = request.data)
        if invernaculo.is_valid():
            invernaculo.save(creado = date.today())
            return Response(invernaculo.data, status = status.HTTP_201_CREATED)
        return Response(invernaculo.errors, status = status.HTTP_400_BAD_REQUEST)


class MaterialEstructuraViewSet(viewsets.ModelViewSet):
    queryset = MaterialEstructura.objects.all()
    serializer_class = MaterialEstructuraSerializer


class AnioConstruccionViewSet(viewsets.ModelViewSet):
    queryset = AnioConstruccion.objects.all()
    serializer_class = AnioConstruccionSerializer


@api_view(['GET','POST','PUT'])
def sincro_cultivo(request):
    """
    API Endpoint que permite listar todos los cultivos
    o crear nuevos cultivos
    """
    if request.method == 'GET':
        cultivos = Cultivo.objects.all()
        serializer = CultivoSerializer(cultivos, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        cultivo = CultivoSerializer(data = request.data)
        if cultivo.is_valid():
            cultivo.save(creado = date.today())
            return Response(cultivo.data, status = status.HTTP_201_CREATED)
        return Response(cultivo.errors, status = status.HTTP_400_BAD_REQUEST)


class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer


class TipoCultivoViewSet(viewsets.ModelViewSet):
    queryset = TipoCultivo.objects.all()
    serializer_class = TipoCultivoSerializer


class TipoProduccionViewSet(viewsets.ModelViewSet):
    queryset = TipoProduccion.objects.all()
    serializer_class = TipoProduccionSerializer


class EleccionCultivoViewSet(viewsets.ModelViewSet):
    queryset = EleccionCultivo.objects.all()
    serializer_class = EleccionCultivoSerializer


@api_view(['GET','POST','PUT'])
def sincro_agroquimico_usado(request):
    """
    API Endpoint que permite listar todos los Agroquimicos usados
    o crear nuevos Agroquimicos usados
    """
    if request.method == 'GET':
        agroquimico_usados = AgroquimicoUsado.objects.all()
        serializer = AgroquimicoUsadoSerializer(agroquimico_usados, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        agroquimico_usado = AgroquimicoUsadoSerializer(data = request.data)
        if agroquimico_usado.is_valid():
            agroquimico_usado.save(creado = date.today())
            return Response(agroquimico_usado.data, status = status.HTTP_201_CREATED)
        return Response(agroquimico_usado.errors, status = status.HTTP_400_BAD_REQUEST)
    queryset = AgroquimicoUsado.objects.all()
    serializer_class = AgroquimicoUsadoSerializer


@api_view(['GET'])
def get_ids_by_transaccion(request,transaccion):

    if request.method == 'GET':
        establecimiento = Establecimiento.objects.get(transaccion = transaccion)
        encuestado      = Encuestado.objects.get(transaccion = transaccion)
        try:
            familia         = Familia.objects.get(transaccion = transaccion)
        except:
            familia = Familia()
        try:    
            agroquimico     = Agroquimico.objects.get(transaccion = idsTransaccion)
        except:
            agroquimico = Agroquimico()

        ids = {
            'establecimiento':establecimiento.id,
            'encuestado':encuestado.id,
            'familia':familia.id,
            'agroquimico':agroquimico.id
        }

        idsTransaccion = IdsTransaccionSerializer(ids)
        return Response(idsTransaccion.data,status = status.HTTP_200_OK)

    return Response(status = status.HTTP_400_BAD_REQUEST)
