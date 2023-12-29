from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    #return HttpResponse("hola Inicio!")
    return render(request,'App1/inicio.html')


def cursos(request):
    #return HttpResponse("hola Cursos!")
    return render(request,'App1/cursos.html')

def profesores(request):
    #return HttpResponse("hola Profesores!")
    return render(request,'App1/profesores.html')

def estudiantes(request):
    #return HttpResponse("hola Estudiantes!")
    return render(request,'App1/estudiantes.html')

def entregables(request):
    #return HttpResponse("hola Entregables!")
    return render(request,'App1/entregables.html')