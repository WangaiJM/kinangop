from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

# About
def about(request):
    return render(request, 'about/about.html')
def vision(request):
    return render(request, 'about/vision.html')

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