from django.shortcuts import render
from .models import Capitulos
# Create your views here.

def Capitulos(request):
    capitulos = Capitulos.objects.all()
    return render(request, 'capitulos.html',{'capitulos': capitulos})