from django.shortcuts import render

def index(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def vision(request):
    return render(request, 'vision.html')