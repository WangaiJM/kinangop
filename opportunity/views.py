from django.shortcuts import render
from .models import tender, career, internship

def tenderView(request):
    tenders = tender.objects.all()
    context = {'tenders':tenders}
    return render(request, 'tenders.html', context)

def careerView(request):
    careers = career.objects.all()
    context = {'careers': careers}
    return render(request, 'careers.html', context)

def internshipView(request):
    internships = internship.objects.all()
    context = {'internships':internships}
    return render(request, 'internships.html', context)