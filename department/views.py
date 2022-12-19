from django.shortcuts import render
from .models import department

def programs(request):
    departments = department.objects.all()
    context = {'departments' : departments }
    return render(request, 'admissions/programs.html', context)

