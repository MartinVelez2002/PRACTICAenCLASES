from django.shortcuts import render
from django.views import *
# Create your views here.
class InicioView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'base.html',{'titulo':'Menu principal', 'url_anterior':'/'})

class PRUEBA(View):
    def get(self, request, *args, **kwargs):
        return render(request,'PRUEBA.html')

