from base.admin import BaseAdmin
from django.utils.html import format_html


class ProveedorAdmin(BaseAdmin):
    list_display = ['ruc', 'razon_social', 'email']
    list_per_page = 10
    list_filter = ['activo', ]
    search_fields = ['id']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']


class CompraAdmin(BaseAdmin):
    list_display = ['id','activo']
    list_per_page = 10
    list_filter = ['activo', ]
    search_fields = ['id']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']


class CompraDetalleAdmin(BaseAdmin):
    list_display = ['id', 'activo']
    list_per_page = 10
    list_filter = ['activo', ]
    search_fields = ['id']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']

class OrdenCompraAdmin(BaseAdmin):
    list_display = ['visor', 'razon_social', 'fecha_creacion', 'usuario_creacion', 'activo' ]
    list_per_page = 10
    list_filter = ['activo']
    search_fields = ['razon_social']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']

    def razon_social(self, obj):
        return obj.proveedor.razon_social

    def visor(self, obj):
        return format_html('<a href="/admin/proveedor/ordencompra/ver_orden?id={id}">{msg}</a>',
            id=obj.id, msg='VER')
    
    

class OrdenCompraDetalleAdmin(BaseAdmin):
    list_display = ['activo']
    list_per_page = 10
    list_filter = ['activo']
    search_fields = ['codigo']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']