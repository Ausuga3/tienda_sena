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
    precio = models.IntegerField()
    stock = models.IntegerField()
    CATEGORIAS = (
        (0, ""),
        (1, "Ropa"),
        (2, "Comida"),
        (3, "Electrodomesticos"),
    )
    categoria = models.IntegerField(choices=CATEGORIAS, default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nombre} - ( {self.stock} unidades)"

class Factura(models.Model):
    fecha = models.DateField(help_text="Fecha de Factura YYYY-MM-DD")
    cliente = models.CharField(max_length=100)
    num_factura = models.IntegerField()
    producto = models.ForeignKey('Producto', on_delete = models.DO_NOTHING)

    def __str__(self):
        return f"{self.num_factura} - {self.cliente}"

# makemigrations tienda
# toma el models.py y crea un pseudoSQL

#migrate
#toma la migracion nueva y la despliega en el motor DB        