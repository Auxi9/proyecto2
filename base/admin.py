from django.forms import TextInput, Textarea
from django.contrib import admin
from datetime import datetime as dt

from .models import *


class BaseAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion_id = request.user.id
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion_id = request.user.id
            obj.fecha_creacion = dt.now()
        obj.save()

    def has_delete_permission(self, request, obj=None):
        return False

    readonly_fields = ('usuario_creacion', 'fecha_creacion',
                       'usuario_modificacion', 'fecha_modificacion')

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})}
    }
