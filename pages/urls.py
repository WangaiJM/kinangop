from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='home'),
    # about
    path('about/', views.aboutView, name='about'),
    path('vision/', views.vision, name='vision'),
    path('service-charter/', views.service_charter, name='service_charter'),
    path('board-of-governors/', views.bogView, name='bogs'),
    path('principal/', views.principalView, name='principal'),
    # admissions
    path('gen-procedure/', views.procedure, name='procedures'),

    path('adminssion-downloads/', views.admissionDownloads, name='admission-downloads'),
    path('online-registration/', views.onlineReg, name='online-registration'),
    # students
    path('student-downloads/', views.studentDownloads, name='student-downloads'),
    path('welfare/', views.welfare, name="welfare"),
    path('dean/', views.deanView, name='dean'),
    # contacts
    path('contacts/', views.contacts, name="contacts"),
]