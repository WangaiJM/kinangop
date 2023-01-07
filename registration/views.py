from django.shortcuts import render
from .forms import registrationForm
from django.http import HttpResponseRedirect

def onlineReg(request):
    if request.method == 'POST':
        form = registrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
            
    else:
        form = registrationForm()

    return render(request, 'admissions/online-reg.html', {'form' : form} )
