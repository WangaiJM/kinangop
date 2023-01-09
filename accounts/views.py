from django.shortcuts import render


def dashboardView(request):
    return render(request, 'accounts/dashboard.html')