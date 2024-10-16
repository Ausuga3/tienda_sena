from django.contrib import admin
# python3 /manage.py createsuperuser
# Register your models here.

from .models import *


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cod', 'nombre', 'precio', 'stock', 'categoria']  
    search_fields = ['nombre', 'cod']
    list_filter = ['categoria']
    list_editable = ['stock', 'categoria']


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'cliente', 'num_factura', 'producto']  
    search_fields = ['num_factura']
    list_filter = ['producto', 'num_factura']
    list_editable = ['fecha', 'producto']


