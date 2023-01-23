from django.urls import path
from . import views

urlpatterns = [
    path('online-registration-success/', views.onlineRegSuccessView,
         name='online-registration-success'),
    path('online-registration/', views.onlineReg, name='online-registration'),
]
