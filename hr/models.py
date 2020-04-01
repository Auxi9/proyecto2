from base.models import Persona


class Empleado(Persona):

    def __str__(self):
        return "{}".format(self.nombre + " " + self.apellido)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'