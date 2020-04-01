from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True,
                                          blank=False,
                                          verbose_name='Creado en fecha')
    usuario_creacion = models.ForeignKey(User, related_name=
                                         '%(class)s_usuario_creacion',
                                         on_delete=models.SET_NULL,
                                         null=True, blank=True,
                                         verbose_name='Creado por')
    fecha_modificacion = models.DateTimeField(null=True, blank=True,
                                              verbose_name=
                                              'Modificado en fecha')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL,
                                related_name='%(class)s_usuario_modificacion',
                                             null=True, blank=True,
                                             verbose_name='Modificado por')
    activo = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        abstract=True


class Persona(Base):

    GENEROS = (
        ("O", "Sin especificar"),
        ("F", "Femenino"),
        ("M", "Masculino"),
    )
    nombre = models.CharField(max_length=70, null=False, blank=False)
    apellido = models.CharField(max_length=70, null=False, blank=False)
    genero = models.CharField(max_length=1, null=False, blank=False,
                              choices=GENEROS, default="O")
    telefono = models.CharField(max_length=50, null=True, blank=True)
    email = models.TextField(max_length=100, null=True, blank=True)


    class Meta:
        abstract=True