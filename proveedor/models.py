from django.db import models
from base.models import Base
from stock.models import Producto


class Proveedor(Base):
    ruc = models.CharField(max_length=50, null=False, blank=False, unique=True)
    razon_social = models.CharField(max_length=500, null=False, blank=False)
    direccion = models.TextField(max_length=500, null=True, blank=True)
    pais = models.TextField(max_length=200, null=True, blank=True)
    ciudad = models.TextField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    email = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.ruc + " - " + self.razon_social)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class OrdenCompra(Base):

    # id_cabecera = models.IntegerField(null=False, blank=False,  default=0)
    proveedor = models.ForeignKey(Proveedor,
                                related_name='%(class)s_proveedor',
                                on_delete=models.CASCADE, null=False,
                                blank=False)
    def __str__(self):
        return "{}".format(self.proveedor)

    class Meta:
        verbose_name = 'ordenCompra'
        verbose_name_plural = 'ordenCompra'

class OrdenCompraDetalle(Base):

    cabecera = models.ForeignKey(OrdenCompra,  related_name='%(class)s_ordencompra',
                                on_delete=models.SET_NULL, null=True, blank=True)
    existente = models.ForeignKey(Producto,
                                related_name='%(class)s_producto',
                                on_delete=models.SET_NULL, null=True,
                                blank=True)
    #codigo = models.IntegerField(null=False, blank=False,  default=0)
    #denominacion = models.CharField(max_length=80, null=False, blank=False, default=0)
    precio_compra = models.BigIntegerField(null=False, blank=False, default=0,
                                           verbose_name='Precio de compra')
    cantidad = models.IntegerField(null=False, blank=False,  default=0)

    def __str__(self):
        return "{}".format(self.denominacion)

    class Meta:
        verbose_name = 'ordenCompraDetalle'
        verbose_name_plural = 'ordenCompraDetalle'


class Compra(Base):
    proveedor = models.ForeignKey(Proveedor, related_name='%(class)s_proveedor',
                                on_delete=models.PROTECT, null=False,
                                blank=False)
    # el modelo ya tiene fecha_creacion (hereda de BASE)
    #fecha_registro = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.fecha_creacion)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class CompraDetalle(Base):
    # el modelo ya tiene fecha_creacion (hereda de BASE)
    #fecha_registro = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    producto = models.ForeignKey(Producto, related_name='%(class)s_producto',
                                on_delete=models.PROTECT, null=False,
                                blank=False)

    def __str__(self):
        return "{}".format(self.fecha_creacion)

    class Meta:
        verbose_name = 'Compra Detalle'
        verbose_name_plural = 'Compras Detalles'
