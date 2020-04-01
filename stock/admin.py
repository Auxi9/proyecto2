from base.admin import BaseAdmin


class ProductoAdmin(BaseAdmin):
    list_display = ['codigo', 'denominacion', 'activo']
    list_per_page = 10
    list_filter = ['activo']
    search_fields = ['codigo']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']