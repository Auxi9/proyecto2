from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect

class AperturaCaja(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return render(request, 'caja/apertura_caja.html')

    def post(self, request, format=None):
        try:
            saldoInicial = request.data.get("saldoInicial", None)
            if saldoInicial is None:
                raise Exception("Saldo Inicial no cargado")

            nuevoSaldoInicial = Caja()
            try:
                nuevoSaldoInicial.save()
            except Exception as e:
                raise e


            return Response({saldoInicial}, status=HTTP_200_OK)
        except Exception as e:
            return Response({}, status=HTTP_400_BAD_REQUEST)