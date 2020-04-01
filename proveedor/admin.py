from base.admin import BaseAdmin

class ProveedorAdmin(BaseAdmin):
    list_display = ['id', 'activo']
    list_per_page = 10
    list_filter = ['activo', ]
    search_fields = ['id']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']


class CompraAdmin(BaseAdmin):
    list_display = ['id', 'activo']
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