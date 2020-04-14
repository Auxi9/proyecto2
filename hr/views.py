from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .models import Empleado


class RegistroEmpleado(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        generos = Empleado.GENEROS
        return render(request, 'hr/registro_empleado.html', context={"generos": generos})

    def post(self, request, format=None):
        try:
            username = request.data.get("username", None)
            if username is None:
                raise Exception("Username no cargado")
            contrasenha = request.data.get("contrasenha", None)
            if contrasenha is None:
                raise Exception("Contrasenha no cargado")
            nombre = request.data.get("nombre", None)
            if nombre is None:
                raise Exception("Nombre no cargado")
            apellido = request.data.get("apellido", None)
            if apellido is None:
                raise Exception("El apellido no puede ser nulo")
            direccion = request.data.get("direccion", None)
            if direccion is None:
                raise Exception("La direccion no puede ser nulo")
            ciudad = request.data.get("ciudad", None)
            if ciudad is None:
                raise Exception("La ciudad no puede ser nulo")
            telefono = request.data.get("telefono", None)
            if telefono is None:
                raise Exception("El telefono no puede ser nulo")
            email = request.data.get("email", None)
            if email is None:
                raise Exception("El email no puede ser nulo")
            genero = request.data.get("genero", None)
            if genero is None:
                raise Exception("El genero no puede ser nulo")

            nuevouser = User()
            nuevouser.username = username
            nuevouser.set_password(contrasenha)
            try:
                nuevouser.save()
            except Exception as e:
                raise e

            nuevoemp = Empleado()
            nuevoemp.usuario_creacion = request.user
            nuevoemp.nombre = nombre
            nuevoemp.apellido = apellido
            nuevoemp.username = username
            nuevoemp.contrasenha = contrasenha
            nuevoemp.direccion = direccion
            nuevoemp.ciudad = ciudad
            nuevoemp.telefono = telefono
            nuevoemp.email = email
            nuevoemp.genero = genero
            nuevoemp.usuario_id = nuevouser.id

            try:
                nuevoemp.save()
            except Exception as e:
                raise e

            return Response({"id": nuevoemp.id}, status=HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)},
                            status=HTTP_400_BAD_REQUEST)