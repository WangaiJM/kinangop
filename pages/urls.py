from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='home'),
    # about
    path('about/', views.aboutView, name='about'),
    path('vision/', views.vision, name='vision'),
    path('service-charter/', views.serviceCharterView, name='service_charter'),
    path('board-of-governors/', views.bogView, name='bogs'),
    path('principal/', views.principalView, name='principal'),
    path('gallery/', views.galleryView, name='gallery'),
    path('carousel/', views.carouselView, name='carousel'),
    # admissions
    path('gen-procedure/', views.procedure, name='procedures'),

    path('adminssion-downloads/', views.admissionDownloads, name='admission-downloads'),
    # students
    path('student-downloads/', views.studentDownloads, name='student-downloads'),
    path('welfare/', views.welfare, name="welfare"),
    path('dean/', views.deanView, name='dean'),
   
]