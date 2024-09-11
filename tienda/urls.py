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
]