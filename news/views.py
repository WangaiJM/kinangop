from django.shortcuts import render
from .models import Latest, Upcoming
from department.models import department_message, department_images

def newsView(request):
    latests = Latest.objects.all().order_by('-created_at')[:6]
    upcomings = Upcoming.objects.all().order_by('-created_at')[:2]
    deptMsg = department_message.objects.all()
    deptImg = department_images.objects.all()
    context = {
        'latests' : latests,
        'upcomings' : upcomings,
        'dept_msgs' : deptMsg,
        'dept_images' : deptImg
    }

    return render(request, 'index.html', context)

def latestView(request):
    latest = Latest.objects.all()
    context = {'latests' : latest}
    return render(request, 'latest/all-latest.html', context)

def upcomingView(request):
    upcoming = Upcoming.objects.all()
    context = {'upcomings' : upcoming}
    return render(request, 'upcoming/all-upcoming.html', context)

def singleLatestView(request, id, slug):
    latest = Latest.objects.get(id = id, slug = slug)
    context = {'latest' : latest}
    return render(request, 'latest/latest.html', context)

def singleUpcomingView(request, id, slug):
    upcoming = Upcoming.objects.get(id = id, slug = slug)
    context = {'upcoming' : upcoming}
    return render(request, 'upcoming/upcoming.html', context)
