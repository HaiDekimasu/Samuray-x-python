from django.urls import path
from . import views

urlpatterns = [
    path('capitulos/', views.Capitulos, name='capitulos')
]
