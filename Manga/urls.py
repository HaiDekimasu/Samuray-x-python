from django.urls import path
from . import views

urlpatterns = [
    path('manga/', views.manga, name='manga')
]
