from django.contrib import admin
from .models import Cliente, Factura, Producto, FacturaProducto

admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Producto)
admin.site.register(FacturaProducto)
