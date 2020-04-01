from django.db import models
from base.models import Base
from crm.models import Cliente
from caja.models import Caja
from proveedor.models import Compra


class Venta(Base):

    estados = (
        ("R", "Registrado"),
        ("E", "Expedido"),
        ("A", "Anulado")
    )
    cliente = models.ForeignKey(Cliente, related_name='%(class)s_cliente',
                                on_delete=models.PROTECT, null=False,
                                blank=False)
    razon_social = models.TextField(max_length=500, null=True, blank=True)
    ruc = models.TextField(max_length=20, null=True, blank=True)
    domicilio = models.TextField(max_length=500, null=True, blank=True)
    ciudad = models.TextField(max_length=200, null=True, blank=True)
    telefono = models.TextField(max_length=50, null=True, blank=True)
    email = models.TextField(max_length=100, null=True, blank=True)
    total_articulos = models.IntegerField(null=False, blank=False)
    monto_impuesto = models.IntegerField(null=False, blank=False)
    monto_total = models.IntegerField(null=False, blank=False)
    pagado_efectivo = models.IntegerField(null=True, blank=True, default=0,
                                          verbose_name="Pagado con efectivo")
    pagado_credito = models.IntegerField(null=True, blank=True, default=0,
                                         verbose_name="Pagado con tarjeta "
                                                      "de crédito")
    pagado_debito = models.IntegerField(null=True, blank=True, default=0,
                                          verbose_name="Pagado con tarjeta "
                                                       "de débito")
    caja = models.ForeignKey(Caja, related_name='%(class)s_caja',
                               on_delete=models.SET_NULL, null=True,
                             blank=True)
    estado = models.CharField(max_length=1, null=False, blank=False,
                              default="R", choices=estados)

    class Meta:
        verbose_name = 'Registro de venta'
        verbose_name_plural = 'Registros de ventas'



class VentaDetalle(Base):

    venta = models.ForeignKey(Venta, on_delete=models.PROTECT,
                              related_name='%(class)s_venta', null=False,
                              blank=False)
    precio_unitario = models.IntegerField(default=1, null=False, blank=False)
    cantidad = models.IntegerField(default=1, null=False, blank=False)
    monto_impuesto = models.FloatField(default=0.0, null=False, blank=False)
    monto_total = models.FloatField(default=0.0, null=False, blank=False)

    class Meta:
        verbose_name = 'Detalle de registro de venta'
        verbose_name_plural = 'Detalles de registros de ventas'


class Pedido(Base):

    fecha = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Carga de productos'
        verbose_name_plural = 'Cargas de productos'


class PedidoDetalle(Base):

    compra = models.ForeignKey(Compra, on_delete=models.PROTECT,
                              related_name='%(class)s_carga', null=False,
                              blank=False)
    denominacion = models.TextField(max_length=100, null=False, blank=False)
    fecha_ingreso = models.TextField(max_length=15, null=True, blank=True,
                                     default="-")
    sku = models.TextField(max_length=50, null=True, blank=True, default="-")
    presentacion = models.IntegerField(default=-1)
    codigo = models.TextField(max_length=50, null=True, blank=True,
                              default="-")
    origen = models.TextField(max_length=50, null=True, blank=True,
                              default="-")
    subcategoria = models.TextField(max_length=50, null=True, blank=True,
                                    default="-")
    color = models.TextField(max_length=50, null=True, blank=True, default="-")
    marca = models.TextField(max_length=50, null=True, blank=True, default="-")
    talle = models.TextField(max_length=50, null=True, blank=True, default="-")
    cantidad = models.TextField(max_length=50, null=True, blank=True,
                                default=0)
    costo_unitario = models.CharField(max_length=20, null=True, blank=True)
    costo_total = models.CharField(max_length=20, null=True, blank=True)
    margen_unitario = models.CharField(max_length=20, null=True, blank=True)
    utilidad_unitaria = models.CharField(max_length=20, null=True, blank=True)
    utilidad_total = models.CharField(max_length=20, null=True, blank=True)
    precio_neto_unitario = models.CharField(max_length=20, null=True, blank=True)
    precio_neto_total = models.CharField(max_length=20, null=True, blank=True)
    fee_unitario = models.CharField(max_length=20, null=True, blank=True)
    neto_y_fee_unitario = models.CharField(max_length=20, null=True, blank=True)
    comision = models.CharField(max_length=20, null=True, blank=True)
    net_y_fee_y_comi = models.CharField(max_length=20, null=True, blank=True)
    iva_unitario = models.CharField(max_length=20, null=True, blank=True)
    total_iva = models.CharField(max_length=20, null=True, blank=True)
    iva_y_unit_y_fee = models.CharField(max_length=20, null=True, blank=True)
    total_general_con_iva = models.CharField(max_length=20, null=True, blank=True)
    comision_unit_tarj = models.CharField(max_length=20, null=True, blank=True)
    precio_venta_unitario = models.CharField(max_length=20, null=True, blank=True)
    ajuste = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'Detalle de carga de productos'
        verbose_name_plural = 'Detalles de carga de productos'
