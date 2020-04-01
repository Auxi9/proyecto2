from base.admin import BaseAdmin


class ClienteAdmin(BaseAdmin):
    list_display = ['ruc', 'razon_social', 'activo']
    list_per_page = 10
    list_filter = ['activo', ]
   # search_fields = ['ruc', 'razon_social']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']

class CarritoAdmin(BaseAdmin):
    list_display = ['monto_total', 'activo']
    list_per_page = 10
    list_filter = ['activo', ]
    #search_fields = ['ruc', 'razon_social']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']

class CarritoItemAdmin(BaseAdmin):
    list_display = ['id', 'activo']
    list_per_page = 10
    list_filter = ['activo', ]
    search_fields = ['id']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']