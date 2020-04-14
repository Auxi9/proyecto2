from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from proveedor.models import Proveedor
from django.db.models import Q
import json


class RegistroOrdenCompra(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return render(request, 'stock/registrar_orden_compra.html')


@api_view(['POST'])
#@csrf_protect
def get_proveedores_reg_orden_compra(request):
    """
        :param buscado - RUC o razón social del proveedor buscado
    """
    #body_unicode = request.body.decode('utf-8')
    #body = json.loads(body_unicode)
    #buscado = body.get("buscado", None)

    buscado = request.POST.get("buscado", None)
    if buscado is None:
        return Response({"error": "Término de búsqueda no indicado"}, status=HTTP_400_BAD_REQUEST)
        # resultados = Proveedor.objects.filter(razon_social__icontains=buscado).all()

    resultados = Proveedor.objects.filter(Q(ruc__icontains=buscado) | Q(razon_social__icontains=buscado)).all()

    encontrados = []
    for prove in resultados:
        encontrados.append({
            "ruc": prove.ruc,
            "razon_social": prove.razon_social,
            "direccion": prove.direccion,
            "telefono": prove.telefono
        })
    return Response({"encontrados": encontrados}, status=HTTP_200_OK)
