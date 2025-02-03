from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    fecha = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Factura {self.id} - {self.cliente.nombre}"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=230, blank=True, null=True)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class FacturaProducto(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.factura} - {self.producto.nombre} ({self.cantidad})"
