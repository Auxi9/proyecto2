from base.admin import BaseAdmin


class EmpleadoAdmin(BaseAdmin):
    list_display = ['nombre', 'apellido', 'activo']
    list_per_page = 10
    list_filter = ['activo']
    search_fields = ['nombre', 'apellido']
    exclude = ['usuario_creacion', 'usuario_modificacion',
               'fecha_modificacion']