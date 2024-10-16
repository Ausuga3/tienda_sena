from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cod', 'nombre', 'precio', 'stock', 'categoria']  
    search_fields = ['nombre', 'cod']
    list_filter = ['categoria']
    list_editable = ['stock', 'categoria']