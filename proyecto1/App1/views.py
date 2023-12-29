from django.shortcuts import render
from django.http import HttpResponse
from App1.forms import FormCurso
from App1.models import Curso

# Create your views here.

def inicio(request):
    #return HttpResponse("hola Inicio!")
    return render(request,'App1/inicio.html')


def cursos(request):
    
    mensaje =""
    cursos = Curso.objects.all()
    cantidad = Curso.objects.count()
    if request.method=='POST':
        formulario = FormCurso(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            curso = Curso(nombre=info['nombre'],camada = info['numero'],detalle=info['detalle'])
            curso.save()
            formulario = FormCurso()
            mensaje ="El Curso se ingresó con éxito. Gracias!"

    else:
        formulario = FormCurso()

    contexto = {"mensaje":mensaje,"cursos":cursos,"cantidad":cantidad,"formulario":formulario}

    return render(request,'App1/cursos.html',contexto)

def profesores(request):
    #return HttpResponse("hola Profesores!")
    return render(request,'App1/profesores.html')

def estudiantes(request):
    #return HttpResponse("hola Estudiantes!")
    return render(request,'App1/estudiantes.html')

def entregables(request):
    #return HttpResponse("hola Entregables!")
    return render(request,'App1/entregables.html')