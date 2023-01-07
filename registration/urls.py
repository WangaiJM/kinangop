from django.urls import path
from . import views

urlpatterns = [
    path('online-registration/', views.onlineReg, name='online-registration'),
]