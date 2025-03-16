from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import *
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
def test(request):
    return HttpResponse("Hello World")
@api_view(['GET'])
def product(request):
    p= WhatsUsers.objects.all()
    print(p[0].image.path)
    data=ProductSerializer(p,many=True).data
    return Response({'data':data})