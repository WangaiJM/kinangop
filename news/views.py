from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Latest, Upcoming

def newsView(request):
    latests = Latest.objects.all().order_by('-created_at')[:6]
    upcomings = Upcoming.objects.all().order_by('-created_at')[:2]
    context = {
        'latests' : latests,
        'upcomings' : upcomings
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
