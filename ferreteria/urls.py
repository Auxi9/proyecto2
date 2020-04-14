"""ferreteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from stock.models import *
from stock.admin import *
from crm.models import *
from crm.admin import *
from caja.models import *
from caja.admin import *
from caja.views import *
from proveedor.models import *
from proveedor.admin import *
from stock.views import *
from venta.models import *
from venta.admin import *
from hr.admin import *
from hr.models import *
from hr.views import *


admin.site.site_header = "FERRETERIA PORVENIR - PANEL DE CONTROL"
admin.site.site_title = "FERRETERIA PORVENIR"
admin.site.index_title = "Secciones"
admin.site.register(Producto, ProductoAdmin)
admin.site.register(OrdenCompra, OrdenCompraAdmin)
admin.site.register(OrdenCompraDetalle, OrdenCompraDetalleAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(CarritoItem, CarritoItemAdmin)
admin.site.register(Caja, CajaAdmin)
admin.site.register(Gasto, GastoAdmin)
admin.site.register(Movimiento, MovimientoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(CompraDetalle, CompraDetalleAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(VentaDetalle, VentaDetalleAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoDetalle, PedidoDetalleAdmin)
admin.site.register(Empleado, EmpleadoAdmin)


urlpatterns = [
    url(r'^api/get_proveedores_reg_orden_compra$', get_proveedores_reg_orden_compra, name='gtroc'),
    url(r'^admin/hr/empleado/add/$', RegistroEmpleado.as_view(), name='empleado_add'),
    url(r'^admin/caja/caja/add/$', AperturaCaja.as_view(), name='caja_abrir'),
    url(r'^admin/stock/ordencompra/add/$', RegistroOrdenCompra.as_view(), name='ordencompra_add'),
    path('admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),
]
