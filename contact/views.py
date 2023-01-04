from django.shortcuts import render
from .forms import contactForm

def contacts(request):
    if request.method == 'POST':
        form = contactForm(request.POST)

        if form.is_valid():
            form = form.save()
            
    else:
        form = contactForm()

    return render(request, 'contacts/contact.html', {'form' : form} )