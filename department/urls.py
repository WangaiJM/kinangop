from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.programs, name='programs'),
]