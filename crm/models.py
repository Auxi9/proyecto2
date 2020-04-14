from django.db import models
from base.models import Base, Persona
from stock.models import Producto


class Cliente(Persona):

    razon_social = models.CharField(max_length=500, null=False, blank=False)
    ruc = models.CharField(max_length=50, null=False, blank=False, unique=True)
    domicilio = models.TextField(max_length=500, null=True, blank=True)
    ciudad = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.ruc + " - " + self.razon_social)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Carrito(Base):

    cliente = models.ForeignKey(Cliente,
                                  related_name='%(class)s_cliente',
                                  on_delete=models.CASCADE, null=False,
                                  blank=False)
    cantidad_articulos = models.CharField(max_length=50, null=True, blank=True)
    monto_total = models.BigIntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return "{}".format(self.cliente.__str__)

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'


class CarritoItem(Base):

    carrito = models.ForeignKey(Carrito,
                                related_name='%(class)s_carrito',
                                on_delete=models.CASCADE, null=False,
                                blank=False)
    producto = models.ForeignKey(Producto,
                                related_name='%(class)s_producto',
                            on_delete=models.CASCADE, null=False,
                                blank=False)
    cantidad = models.CharField(max_length=50, null=True, blank=True)
    monto_unitario = models.BigIntegerField(null=False, blank=False, default=0)
    monto_total = models.BigIntegerField(null=False, blank=False, default=0)


    def __str__(self):
        return "{}".format(self.producto)


    class Meta:
        verbose_name = 'CarritoItem'
        verbose_name_plural = 'CarritosItem'