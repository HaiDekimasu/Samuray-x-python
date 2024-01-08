from django.shortcuts import render
from .models import Manga

# Create your views here.
def manga(request):
    manga = Manga.objects.all()
    return render(request, 'manga.html', {'manga': manga})