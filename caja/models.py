from django.db import models
from base.models import Base

class Caja(Base):

    fecha_apertura = models.DateTimeField(null=False, blank=False)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    saldo_apertura = models.IntegerField(null=False, blank=False, default=0)
    saldo_cierre = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return "{}".format(self.fecha_apertura.strftime("%d-%M-%y"))

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'

class Gasto(Base):
    caja = models.ForeignKey(Caja, related_name='%(class)s_caja',
                             on_delete=models.PROTECT, null=False,
                             blank=False)
    motivo = models.CharField(max_length=20, null=False, blank=False,
                              default="Sin especificar")
    descripcion = models.CharField(max_length=100, null=False, blank=False,
                                   default="Sin especificar")
    monto = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'


class Movimiento(Base):

    caja = models.ForeignKey(Caja, related_name='%(class)s_caja',
                                 on_delete=models.PROTECT, null=False,
                             blank=False)
    monto_ingreso = models.IntegerField(default=0, null=False, blank=False)
    monto_egreso = models.IntegerField(default=0, null=False, blank=False)
    entidad = models.CharField(max_length=20, null=False, blank=False)
    id_entidad = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
