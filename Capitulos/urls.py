from django.urls import path
from . import views

urlpatterns = [
    path('capitulos/', views.index, name='capitulos')
]
