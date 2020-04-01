from django.db import models
from base.models import Base
from crm.models import Cliente
from stock.models import Producto

class Proveedor(Base):
    razon_social = models.CharField(max_length=500, null=False, blank=False)
    ruc = models.CharField(max_length=50, null=False, blank=False, unique=True)
    domicilio = models.TextField(max_length=500, null=True, blank=True)
    pais = models.TextField(max_length=200, null=True, blank=True)
    ciudad = models.TextField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    email = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.ruc + " - " + self.razon_social)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Compra(Base):
    cliente = models.ForeignKey(Cliente, related_name='%(class)s_cliente',
                                on_delete=models.PROTECT, null=False,
                                blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.fecha_registro)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class CompraDetalle(Base):
    cliente = models.ForeignKey(Cliente, related_name='%(class)s_cliente',
                                on_delete=models.PROTECT, null=False,
                                blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    producto = models.ForeignKey(Producto, related_name='%(class)s_cliente',
                                on_delete=models.PROTECT, null=False,
                                blank=False)

    def __str__(self):
        return "{}".format(self.fecha_registro)

    class Meta:
        verbose_name = 'Compra Detalle'
        verbose_name_plural = 'Compras Detalles'
