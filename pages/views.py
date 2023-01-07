from django.shortcuts import render
from .models import about, statement, principal, board_of_governor, dean, service_charter, gallery


def index(request):
    return render(request, 'home.html')

# About
def aboutView(request):
    abouts = about.objects.last()
    context = {'about' : abouts}
    return render(request, 'about/about.html', context)

def vision(request):
    statements = statement.objects.last()
    context = {'statement': statements}
    return render(request, 'about/vision.html', context)

def bogView(request):
    bogs = board_of_governor.objects.last()
    context = {'bog' : bogs}
    return render(request, 'about/bogs.html', context)

def principalView(request):
    principals = principal.objects.last()
    context = {'principal': principals}
    return render(request, 'about/principal.html', context)

def deanView(request):
    deans = dean.objects.last()
    context = {'dean': deans}
    return render(request, 'students/dean.html', context)

def serviceCharterView(request):
    services = service_charter.objects.all()
    context = {'services' : services}
    return render(request, 'about/service_charter.html', context)

def galleryView(request):
    galleries = gallery.objects.all().order_by('-uploaded_at')
    context = {'galleries' : galleries}
    return render(request, 'gallery/gallery.html', context)

# Admissions
def procedure(request):
    return render(request, 'admissions/procedure.html')

def admissionDownloads(request):
    return render(request, 'admissions/admission-downloads.html')

# students
def studentDownloads(request):
    return render(request, 'students/student-downloads.html')
def welfare(request):
    return render(request, 'students/welfare.html')
