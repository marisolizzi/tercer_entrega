from django.shortcuts import render
from django.http import HttpResponse
from App1.forms import FormCurso,FormEstudiante,FormProfesor,FormEntregable,FormBuscador
from App1.models import Curso,Estudiante,Profesor,Entregable

# Create your views here.

def inicio(request):
    cursos = []
    busqueda = ""
    formulario = FormBuscador()
    cantidad = 0

    if request.method=='POST':
       formulario = FormBuscador(request.POST)
       if formulario.is_valid():
            info = formulario.cleaned_data
            busqueda = info['nombre_curso']
            cursos = Curso.objects.filter(nombre__icontains=busqueda)
            cantidad = cursos.count()

    contexto = {"busqueda":busqueda,"cursos":cursos,"cantidad":cantidad,"formulario":formulario}

    return render(request,'App1/inicio.html',contexto)


def cursos(request):
    
    mensaje =""
    
    if request.method=='POST':
        formulario = FormCurso(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            curso = Curso(nombre=info['nombre'],camada = info['numero'],detalle=info['detalle'])
            curso.save()
            formulario = FormCurso()
            mensaje ="El Curso se ingresó con éxito. Gracias!"
        else:
            mensaje ="La información ingresada no es correcta. Inténtalo de nuevo!"
    else:
        formulario = FormCurso()

    cursos = Curso.objects.all()
    cantidad = Curso.objects.count()

    contexto = {"mensaje":mensaje,"cursos":cursos,"cantidad":cantidad,"formulario":formulario}

    return render(request,'App1/cursos.html',contexto)

def profesores(request):
    mensaje =""
    if request.method=='POST':
        formulario = FormProfesor(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            curso = Profesor(nombre=info['nombre'],apellido = info['apellido'],email=info['email'],profesion=info['profesion'])
            curso.save()
            formulario = FormProfesor()
            mensaje ="El Profesor se ingresó con éxito. Gracias!"
        else:
            mensaje ="La información ingresada no es correcta. Inténtalo de nuevo!"
    else:
        formulario = FormProfesor()

    profesores = Profesor.objects.all()
    cantidad = Profesor.objects.count()

    contexto = {"mensaje":mensaje,"profesores":profesores,"cantidad":cantidad,"formulario":formulario}

    return render(request,'App1/profesores.html',contexto)

def estudiantes(request):
    mensaje =""
    if request.method=='POST':
        formulario = FormEstudiante(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            curso = Estudiante(nombre=info['nombre'],apellido = info['apellido'],email=info['email'])
            curso.save()
            formulario = FormEstudiante()
            mensaje ="El Estudiante se ingresó con éxito. Gracias!"
        else:
            mensaje ="La información ingresada no es correcta. Inténtalo de nuevo!"
    else:
        formulario = FormEstudiante()

    estudiantes = Estudiante.objects.all()
    cantidad = Estudiante.objects.count()

    contexto = {"mensaje":mensaje,"estudiantes":estudiantes,"cantidad":cantidad,"formulario":formulario}

    return render(request,'App1/estudiantes.html',contexto)

def entregables(request):
    mensaje =""
    if request.method=='POST':
        formulario = FormEntregable(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            curso = Entregable(nombre=info['nombre'],fechaDeEntrega=info['fechaDeEntrega'],entregado=info['entregado'],detalle=info['detalle'])
            curso.save()
            formulario = FormEntregable()
            mensaje ="El Entregable se ingresó con éxito. Gracias!"
        else:
            mensaje ="La información ingresada no es correcta. Inténtalo de nuevo!"
    else:
        formulario = FormEntregable()

    entregables = Entregable.objects.all()
    cantidad = Entregable.objects.count()

    contexto = {"mensaje":mensaje,"entregables":entregables,"cantidad":cantidad,"formulario":formulario}

    return render(request,'App1/entregables.html',contexto)