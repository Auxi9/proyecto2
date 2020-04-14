from django.db import models
from base.models import Base


class Producto(Base):

    codigo = models.IntegerField(null=False, blank=False,  default=0)
    denominacion = models.CharField(max_length=80, null=False, blank=False, default=0)
    precio_compra = models.BigIntegerField(null=False, blank=False, default=0,
                                           verbose_name='Precio de compra')
    precio_venta = models.BigIntegerField(null=False, blank=False, default=0,
                                          verbose_name='Precio de venta')
    precio_descuento = models.BigIntegerField(null=False, blank=False,
                                              default=0)
    porcentaje_descuento = models.BigIntegerField(null=True, blank=False, default=0)
    cantidad = models.IntegerField(null=False, blank=False,  default=0)

    def __str__(self):
        return "{}".format(self.codigo)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

