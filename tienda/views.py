from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db import IntegrityError

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

def sumar_formulrio(request):
    if request.method == "POST":
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        # return HttpResponse(f"La suma de {n1} + {n2} es <strong>{n1+n2}</strong>") 
        contexto = {
            "num1":n1,
            "num2":n2,
            "respuesta": n1+n2
        }
        return render(request,"sumar_respuesta.html", contexto)
    

    else:
        return render(request,"sumar_formulrio.html")
    


#CRUD de Productos

def productos(request):
    #select * from
    #all(Todos), filter(Alguno), get(Uno solo)
    q = Producto.objects.all()
    contexto = {
        "data": q
        }

    return render(request, "productos/listar_productos.html", contexto)


def eliminar_producto(request, id_producto):
    try:

        q = Producto.objects.get(pk = id_producto)
        q.delete()
        messages.success(request, "Producto eliminado correctamente...")
    
    except IntegrityError:
        messages.warning(request, "Error el producto esta relacionado a otra tabla")
    except Producto.DoesNotExist:
        messages.error(request, "El producto no existe")       
    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect("productos")


def agregar_producto(request):
    if request.method == "POST":
        cod = request.POST.get('cod')
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        CATEGORIAS = request.POST.get('categoria')
        try:
            q = Producto(
                cod = cod,
                nombre = nombre,
                precio = precio,
                stock = stock,
                categoria = CATEGORIAS
            )
            q.save()
            messages.success(request, "El producto se ha guardado correctamente!!")
        except Exception as e:
            messages.error(request, f"Error {e}!")
        return redirect("productos")    
    else:
        return render(request,"productos/crear_productos.html")
        
    

def editar_producto(request, id_producto):
    if request.method=='POST':
        #procesar datos
        if request.method == "POST":
            q = Producto.objects.get(pk = id_producto)
            cod = request.POST.get('cod')
            nombre = request.POST.get('nombre')
            precio = request.POST.get('precio')
            stock = request.POST.get('stock')
            CATEGORIAS = request.POST.get('categoria')
            try:
                
                q.cod = cod
                q.nombre = nombre
                q.precio = precio
                q.stock = stock
                q.categoria = CATEGORIAS
                q.save()
                messages.success(request, "El producto se ha actualizado correctamente!!")
                
            except Exception as e:
                messages.error(request, f"Error {e}!")
            return redirect("productos")
    else:
        # mostrar el formulario enviano datos del producto consultado
        q = Producto.objects.get(pk = id_producto)
        return render(request,"productos/crear_productos.html", {"dato": q})