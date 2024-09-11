#URL DE <<<TIENDA>>>

from django.urls import path
from . import views


urlpatterns =[
    path("", views.index, name="index"),
    path("prueba/", views.prueba, name="prueba"),
    path("user/", views.user, name="user"),
]