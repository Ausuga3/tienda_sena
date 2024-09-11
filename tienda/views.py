from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#vistas basadas en funciones

def prueba(request):
    return HttpResponse("<h1 style='color:#000FFF;'>Hola mundo!!</h1>"
                        "<a href='../user/'>User</>")


def user(request):
    #Tag de url a traves de alias {% url 'prueba'%}
    return HttpResponse("<h1 style='color:Green;'>Andres Usuga!!</h1>" "<a href='../prueba/'>prueba</a>")

def index(request):
    #return HttpResponse("Este es el index")
    return render(request,"index.html")


def saludar(request, apellido):
    return HttpResponse(f"Hola {apellido}")


def suma(request,num1,num2):
    return HttpResponse(f"resultado: {num1+num2}")

def encuesta_form(request):
    return render(request,"formulario_encuesta.html")

def procesar_encuesta(request):
    nombre = request.POST.get("name")
    tiene_hambre = request.POST.get("hambre")
    return HttpResponse(f"Su nombre es: <b>{nombre}</b> y <b>{tiene_hambre}</b> tiene hambre!!")