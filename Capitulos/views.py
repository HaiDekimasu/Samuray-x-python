from django.shortcuts import render

# Create your views here.

def Capitulos(request):
    return render(request, 'capitulos.html')