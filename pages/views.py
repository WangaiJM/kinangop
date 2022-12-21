from django.shortcuts import render
from .models import about, statement, principal, board_of_governor


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

def service_charter(request):
    return render(request, 'about/service_charter.html')

# Admissions
def procedure(request):
    return render(request, 'admissions/procedure.html')
def programs(request):
    return render(request, 'admissions/programs.html')
def admissionDownloads(request):
    return render(request, 'admissions/admission-downloads.html')
def onlineReg(request):
    return render(request,'admissions/online-reg.html')
# students
def studentDownloads(request):
    return render(request, 'students/student-downloads.html')
def welfare(request):
    return render(request, 'students/welfare.html')
# contacts
def contacts(request):
    return render(request, 'contacts/contact.html')