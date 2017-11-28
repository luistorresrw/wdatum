# -*-coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from principal.forms import *
from .models import *
from datetime import date
import xlwt

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

        row.append("Si" if encuesta.agroquimico.usa else "No")
        row.append(encuesta.agroquimico.asesoramiento.descripcion)
        row.append(encuesta.agroquimico.tripleLavado.descripcion)


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
    if request.user.is_authenticated():#si el usuario esta autenticado redirecciona a la pagina principal
        return HttpResponseRedirect(reverse('principal'))
    form = LoginForm()#declaramos una variable que reciba los campos del formulario
    mensaje = '' #declaramos una variable con un mensaje vacio
    user = None #declaro la variable user a None
    if request.method == 'POST':#validamos que los datos vengan por Post
        form = LoginForm(request.POST)#le pasamos el request a loginForm
        if form.is_valid(): #verificamos que el formato de los datos sea correcto
            usuario = form.data['user']#asignamos a los datos de usuario a una variable usuario
            password = form.cleaned_data['password']#asignamos a los datos de password a una variable password
            user = authenticate(username = usuario, password = password)#validamos que el usuario y la contraseña sean correctos
            if user is not None:
                request.session['user'] = usuario
                request.session['password'] = password
                auth_login(request, user)
                return HttpResponseRedirect('principal')
            else:
                mensaje = 'Usuario y/o password incorrecto, verifíquelo e inténtelo nuevamente.'
        else:
            mensaje = 'Debe completar ambos campos.'#mandamos un mensaje de error
    context = {
        'form' : form,
        'mensaje' : mensaje,
    }
    return render(request, 'login.html', context)

@login_required
def logout(request):
    auth_logout(request) #cierra sesion
    request.session.flush()
    return redirect(reverse('login'))#redirecciona a login

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


def principal(request):
    lista = Establecimiento.objects.all()
    context = {
		'lista':lista,
	}
    return render(request, 'principal.html', context)

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
                mensaje = "El usuario se creo correctamente."

            except:
                mensaje = "Error al crear el usuario."
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
            usuario.is_active = form.cleaned_data['is_active']
            usuario.save()
            return redirect('crear_usuario')
        else:
            form = UsuarioForm(instance=usuario)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)

    context = {
    'lista':lista,
    'form':form
    }
    return render(request, 'editar_usuario.html', context)

@login_required
def borrar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.is_active = False
    usuario.save()
    return redirect('crear_usuario')

# ---------------Nacionalidad---------------------#

@login_required
def crear_nacionalidad(request):
    lista = Nacionalidad.objects.all().order_by('-is_active')#ordena el listado por es activo
    mensaje=''#declaro un mensaje vacio
    if request.method == 'POST':
        form = NacionalidadForm(request.POST)
        if form.is_valid():
            try:
                form.save()#guarda
                form = NacionalidadForm()#crea un formulario vacio para que el template este limpio luego de crear un usuario
                mensaje = "La nacionalidad de creo correctamente."
            except:
                mensaje = "Error al crear la nacionalidad"

    else:
        form = NacionalidadForm()
    context = {'lista': lista, 'form': form, 'mensaje':mensaje }
    return render(request, 'crear_nacionalidad.html', context)

@login_required
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
    if request.method == 'GET':
        form = NacionalidadForm(instance=nacionalidad)
    context = {'lista': lista, 'form': form, }
    return render(request, './editar_nacionalidad.html', context)

@login_required
def borrar_nacionalidad(request, id):
    nacionalidad = get_object_or_404(Nacionalidad, id=id)

    nacionalidad.is_active=False
    nacionalidad.save()
    return redirect('crear_nacionalidad')

# ------------Nivel de Instruccion-------------------

@login_required
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

@login_required
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

@login_required
def borrar_nivel_instruccion(request, id):
    nivel_instruccion = get_object_or_404(NivelInstruccion, id=id)
    nivel_instruccion.delete()
    nivel_instruccion.is_active = False
    nivel_instruccion.save()
    return redirect('crear_nivel_instruccion')

# ------------Regimen de Tenencia-------------------

@login_required
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

@login_required
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

@login_required
def borrar_regimen_tenencia(request, id):
    regimen_tenencia = get_object_or_404(RegimenTenencia, id=id)
    regimen_tenencia.is_active = False
    regimen_tenencia.save()
    return redirect('crear_regimen_tenencia')

# ------------Año de construcción----------------------

@login_required
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

@login_required
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

@login_required
def borrar_anio_construccion(request, id):
    anio_construccion = get_object_or_404(AnioConstruccion, id=id)
    anio_construccion.is_active = False
    anio_construccion.save()
    return redirect('crear_anio_construccion')

# -----------Material Estructura-----------------------

@login_required
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

@login_required
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

@login_required
def borrar_material_estructura(request, id):
    material_estructura = get_object_or_404(MaterialEstructura, id=id)
    material_estructura.is_active=False
    material_estructura.save()
    return redirect('crear_material_estructura')

# -----------Tipo de Producción -----------------------

@login_required
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

@login_required
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

@login_required
def borrar_tipo_produccion(request, id):
    tipo_produccion = get_object_or_404(TipoProduccion, id=id)
    tipo_produccion.delete()
    return redirect('crear_tipo_produccion')

# -----------Eleccion de Cultivo ------------------------

@login_required
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
            return redirect('crear_eleccion_cultivo')
        else:
            form = EleccionCultivoForm(instance=eleccion_cultivo)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_eleccion_cultivo.html', context)

@login_required
def borrar_eleccion_cultivo(request, id):
    eleccion_cultivo = get_object_or_404(EleccionCultivo, id=id)
    eleccion_cultivo.delete()
    return redirect('crear_eleccion_cultivo')

# -----------Tipo de Cultivo ------------------------

@login_required
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
            return redirect('crear_tipo_cultivo')
        else:
            form = TipoCultivoForm(instance=tipo_cultivo)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_tipo_cultivo.html', context)

@login_required
def borrar_tipo_cultivo(request, id):
    tipo_cultivo = get_object_or_404(TipoCultivo, id=id)
    tipo_cultivo.delete()
    return redirect('crear_tipo_cultivo')

# ------------------Especie ----------------------------

@login_required
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

@login_required
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
            return redirect('crear_factor_climatico')
        else:
            form = EspecieForm(instance=factor_climatico)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_factor_climatico.html', context)

@login_required
def borrar_factor_climatico(request, id):
    factor_climatico= get_object_or_404(FactorClimatico, id=id)
    factor_climatico.delete()
    return redirect('crear_factor_climatico')

# ----------------Triple Lavado-----------------------

@login_required
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
            return redirect('crear_triple_lavado')
        else:
            form = TripleLavadoForm(instance=triple_lavado)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_triple_lavado.html', context)

@login_required
def borrar_triple_lavado(request, id):
    triple_lavado= get_object_or_404(TripleLavado, id=id)
    triple_lavado.delete()
    return redirect('crear_triple_lavado')

# ----------------Asesoramiento-----------------------

@login_required
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
            return redirect('crear_asesoramiento')
        else:
            form = AsesoramientoForm(instance=asesoramiento)
    context = {'lista': lista, 'form': form}
    return render(request, './editar_asesoramiento.html', context)

@login_required
def borrar_asesoramiento(request, id):
    asesoramiento = get_object_or_404(Asesoramiento, id=id)
    asesoramiento.delete()
    return redirect('crear_asesoramiento')



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


@api_view(['GET','POST'])
def sincroEncuestado(request):
    """
    API endpoint que Lista todos los encuestados o Crea nuevos
    """

    if request.method == "GET":
        encuestados = Encuestado.objects.all()
        serializer = EncuestadoSerializer(encuestados,many=True)
        return Response(serializer.data)
    elif request.method == "POST":

        serializer = EncuestadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def sincroEstablecimiento(request):
    """
    API endpoint que lista todos los establecimientos o crea nuevos
    """

    if request.method == 'GET':
        establecimientos = Establecimiento.objects.all()
        serializer = EstablecimientoSerializer(establecimientos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EstablecimientoSerializer(data=request.data,files=request.files)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def sincroFamilia(request):
    """
    API endpoint que lista todos los registros de familia
    o crea un nuevo registro en la base de datos
    """
    if request.method == 'GET':
        familias = Familia.objects.all()
        serializer = FamiliaSerializer(familias,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FamiliaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
