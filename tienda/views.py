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