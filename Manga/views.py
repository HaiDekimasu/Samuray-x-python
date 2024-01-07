from django.shortcuts import render

# Create your views here.
def Manga(request):
    return render(request, 'manga.html')