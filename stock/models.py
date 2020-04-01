from django.db import models
from base.models import Base


class Producto(Base):

    """GENEROS = (
        ("F", "Femenino"),
        ("M", "Masculino"),
        ("O", "Sin especificar")
    )"""
    codigo = models.IntegerField(null=False, blank=False,  default=0)
    denominacion = models.CharField(max_length=80, null=False, blank=False, default=0)
    precio_compra = models.BigIntegerField(null=False, blank=False, default=0,
                                           verbose_name='Precio de compra')
    precio_venta = models.BigIntegerField(null=False, blank=False, default=0,
                                          verbose_name='Precio de venta')
    precio_descuento = models.BigIntegerField(null=False, blank=False,
                                              default=0)
    porcentaje_descuento = models.BigIntegerField(null=True, blank=False, default=0)
    #apellido = models.CharField(max_length=70, null=True, blank=True)
    #genero = models.CharField(max_length=1, null=False, blank=False,
    #                          choices=GENEROS, default="O")
    #razon_social = models.CharField(max_length=500, null=False, blank=False)
    #rut = models.CharField(max_length=50, null=False, blank=False, unique=True)
    #domicilio = models.TextField(max_length=500, null=True, blank=True)
    #ciudad = models.TextField(max_length=200, null=True, blank=True)
    #comuna = models.TextField(max_length=200, null=True, blank=True)
    #giro = models.TextField(max_length=500, null=True, blank=True)
    #telefono = models.CharField(max_length=50, null=True, blank=True)
    #email = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.codigo)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'