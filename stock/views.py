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
from stock.models import Producto
import json
