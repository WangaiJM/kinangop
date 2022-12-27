from django.urls import path
from . import views

urlpatterns = [
    path('careers/', views.careerView, name='careers'),
    path('tenders/', views.tenderView, name='tenders'),
    path('internships/', views.internshipView, name='internships'),
]