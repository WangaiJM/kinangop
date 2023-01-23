from django.shortcuts import render
from .forms import registrationForm


def onlineReg(request):
    if request.method == 'POST':
        form = registrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'online_send_success.html')

    else:
        form = registrationForm()

    return render(request, 'admissions/online-reg.html', {'form': form})


def onlineRegSuccessView(request):
    return render(request, 'online_send_success.html')
