from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='home'),
    # about
    path('about/', views.about, name='about'),
    path('vision/', views.vision, name='vision'),
    # admissions
    path('gen-procedure/', views.procedure, name='procedures'),
    path('programs/', views.programs, name='programs'),
    path('adminssion-downloads/', views.admissionDownloads, name='admission-downloads'),
    path('online-registration/', views.onlineReg, name='online-registration'),
    # students
    path('student-downloads/', views.studentDownloads, name='student-downloads'),
    path('welfare/', views.welfare, name="welfare"),
    # contacts
    path('contacts/', views.contacts, name="contacts"),
]