from django.db import models

# Create your models here.

#ORM: Objecct Relational Mapping.
# Migrations - proceso de convertir una clase en tabla DB.
# models - Es la tab   la.
# Resgistros - objetos.
# Campos - atributo de clase.
# Métdos: puedo calcular cosas, usarlas como campos.


class Producto(models.Model):
    cod = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=254)
    Precio = models.IntegerField()


# makemigrations tienda
# toma el models.py y crea un pseudoSQL

#migrate
#toma la migracion nueva y la despliega en el motor DB        