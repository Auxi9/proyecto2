from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from proveedor.models import Proveedor, OrdenCompra, OrdenCompraDetalle
from django.db.models import Q
from stock.models import Producto
import json


class RegistroOrdenCompra(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return render(request, 'stock/registrar_orden_compra.html')

    def post(self, request, format=None):
        try:
            listaProductos = request.data.get('lista_productos', None)
            if listaProductos is None:
                raise Exception("Listado de productos no cargado")
            listaProductos = json.loads(listaProductos)
            
            proveedor = request.data.get("proveedor", None)
            print("Proveedor con id: " + str(proveedor))
            if proveedor is None:
                raise Exception ("Proveedor no cargado")

            # tenemos todo y hay que procesar
            # crear cabecera orden compra, crear detalles y asignar id de cab
            cabecera = OrdenCompra()
            cabecera.proveedor_id = int(proveedor)
            cabecera.usuario_creacion = request.user

            try:
                cabecera.save()
            except Exception as e:
                raise e

            for pk in listaProductos:
                #pk: id del producto        
                aux = OrdenCompraDetalle()
                aux.existente_id = int(pk)
                aux.precio_compra = listaProductos[pk]['precio_compra']
                aux.cantidad = listaProductos[pk]['cantidad']
                aux.usuario_creacion = request.user
                aux.cabecera_id = cabecera.id
                aux.save()
            
            return Response({}, status=HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)


class RegistroProducto(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return render(request, 'stock/registrar_producto.html')

    def post(self, request, format=None):
        try:
            codigo_barra = request.data.get("cod_barra", None)
            if codigo_barra is None:
                raise Exception("Codigo de barra no cargado")
            denominacion = request.data.get("denominacion", None)
            if denominacion is None:
                raise Exception("Denominacion no cargado")
            precio_compra = request.data.get("prec_compra", None)
            if precio_compra is None:
                raise Exception("Precio compra no cargado")
            precio_venta = request.data.get("prec_venta", None)
            if precio_venta is None:
                raise Exception("Precio venta no cargado")
            #preguntar que onda con el precio descuento que puede ser NULO
            cantidad = request.data.get("cantidad", None)
            if cantidad is None:
                raise Exception("Cantidad no cargada")

            nuevoprod = Producto()
            nuevoprod.usuario_creacion = request.user
            nuevoprod.codigo = codigo_barra
            nuevoprod.denominacion = denominacion
            nuevoprod.precio_compra = precio_compra
            nuevoprod.precio_venta = precio_venta
            #nuevoprod.precio_descuento = precio_descuento
            nuevoprod.cantidad = cantidad

            try:
                nuevoprod.save()
            except Exception as e:
                raise e

            return Response({"id": nuevoprod.id}, status=HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)


def ver_detalle_orden_compra(request):
    id = request.GET.get("id", None)
    cabecera = OrdenCompra.objects.get(id=id)
    detalles = OrdenCompraDetalle.objects.filter(cabecera_id=cabecera.id).all()
    return render(request, 'stock/visualizar_detalleOrdenCompra.html', 
        context={
            "cabecera": cabecera,
            "detalles": detalles
        })


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
            "id": prove.id,
            "ruc": prove.ruc,
            "razon_social": prove.razon_social,
            "direccion": prove.direccion,
            "telefono": prove.telefono
        })
    return Response({"encontrados": encontrados}, status=HTTP_200_OK)



@api_view(['POST'])
#@csrf_protect
def get_producto_reg_orden_compra(request):
   # body_unicode = request.body.decode('utf-8')
    #body = json.loads(body_unicode)

    prodBus = request.POST.get("prodBus", None)
    if prodBus is None:
        return Response({"error": "Término de búsqueda no indicado"}, status=HTTP_400_BAD_REQUEST)

    resultado = Producto.objects.filter(Q(codigo__icontains=prodBus) | Q(denominacion__icontains=prodBus)).all()

    prodEncontrados = []
    for prod in resultado:
        prodEncontrados.append({
            "id": prod.id,
            "codigo": prod.codigo,
            "denominacion": prod.denominacion,
            "precio_compra": prod.precio_compra
        })
    return Response({"prodEncontrados": prodEncontrados}, status=HTTP_200_OK)