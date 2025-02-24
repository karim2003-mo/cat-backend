from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

from .models import Design
# Create your views here.
def test(request):
    return HttpResponse("Hello World")
def alldesigns(request):
    designs = Design.objects.all()
    d=[]
    for design in designs:
        d.append({
            "designername":design.designername,
            "designerexp":design.designerexp,
            "designtype":design.designtype,
            "designrate":design.designrate,
            "designsubrate":design.designsubrate,
            "designimages":design.designimages
        })
    return JsonResponse({"designs":d})
