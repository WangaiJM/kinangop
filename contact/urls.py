from django.urls import path
from . import views

urlpatterns = [
 # contacts
    path('contacts/', views.contacts, name="contacts"),
]