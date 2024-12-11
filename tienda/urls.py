#URL DE <<<TIENDA>>>

from django.urls import path
from . import views


urlpatterns =[
    path("", views.index, name="index"),
    path("prueba/", views.prueba, name="prueba"),
    path("user/", views.user, name="user"),
    path("saludar/<str:apellido>",views.saludar, name="saludar"),
    path("suma/<int:num1>/<int:num2>/", views.suma, name="suma"),
    path("encuesta_form/", views.encuesta_form, name="encuesta_form"),
    path("procesar_encuesta/", views.procesar_encuesta, name="procesar_encuesta"),
    path("sumar_formulrio/", views.sumar_formulrio, name="sumar_formulrio"),
    #CRUD Productos
    path("productos/", views.productos, name="productos"),
    path("eliminar_producto/<int:id_producto>/", views.eliminar_producto, name="eliminar_producto"),
    path("agregar_producto",views.agregar_producto, name="agregar_producto"),
    path("editar_producto/<int:id_producto>/", views.editar_producto, name="editar_producto")
]