from django.urls import path
from . import views

urlpatterns = [
    path('student-login/', views.student_login, name='student-login'),
    path('staff-login/', views.staff_login, name='staff-login'),
    path('staff-dashboard/', views.staff_dashboard, name='staff-dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student-dashboard'),
]