from django.shortcuts import render
from .models import Manga

# Create your views here.
def manga(request):
    mangas = Manga.objects.all()
    return render(request, 'manga.html', {'mangas': mangas})