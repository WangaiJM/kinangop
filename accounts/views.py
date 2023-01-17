from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy


def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            
            if user is not None:
                try:
                    if user.student_profile.is_student:
                        login(request, user)
                        return redirect('student-dashboard')
                except:
                    messages.error(request, "Unathorized Access")
                    return redirect('student-login')
        else:
            messages.error(request, "Invalid Username and/or Password")
            return redirect('student-login')


    form = AuthenticationForm()
    context = { 'login_form' : form }
    return render(request, 'logins/student-login.html', context)

def staff_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            
            if user is not None:
                try:
                    if user.trainer_profile.is_trainer:
                        login(request, user)
                        return redirect('staff-dashboard')
                except:
                    messages.error(request, "Unathorized Access")
                    return redirect('staff-login')
        else:
            messages.error(request, "Invalid Username and/or Password")
            return redirect('staff-login')

    form = AuthenticationForm()
    context = { 'login_form' : form }
    return render(request, 'logins/staff-login.html', context)

def staff_dashboard(request):
    return render(request, 'accounts/staff-dashboard.html')

def student_dashboard(request):
    return render(request, 'accounts/student-dashboard.html')