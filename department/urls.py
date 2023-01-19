from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.programsView, name='programs'),
    path('department/<str:dept_id>/<str:dept_name>', views.departmentView, name='single-department'),
]