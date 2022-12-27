from django.shortcuts import render
from .models import tender, career, internship

def tenderView(request):
    tenders = tender.objects.all().order_by('-uploaded_at')
    context = {'tenders':tenders}
    return render(request, 'tenders.html', context)

def careerView(request):
    careers = career.objects.all().order_by('-uploaded_at')
    context = {'careers': careers}
    return render(request, 'careers.html', context)

def internshipView(request):
    internships = internship.objects.all().order_by('-uploaded_at')
    context = {'internships':internships}
    return render(request, 'internships.html', context)
