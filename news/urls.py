from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsView, name='home'),
    path('all-latest/', views.latestView, name="all-latest"),
    path('all-upcoming/', views.upcomingView, name="all-upcoming"),
    path('latest/<str:id>/<slug:slug>', views.singleLatestView, name="single-latest"),
    path('upcoming/<str:id>/<slug:slug>', views.singleUpcomingView, name="single-upcoming"),
]