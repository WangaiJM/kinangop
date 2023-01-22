from django.shortcuts import render, redirect
from .forms import contactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string


def contacts(request):
    if request.method == 'POST':
        form = contactForm(request.POST)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            message = f"""
                Name: {firstname} {lastname}
                Email: {email}
                Query: {body}
            """

            html = render_to_string('contacts/content.html', {
                'subject': subject,
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'subject': subject,
                'body': body,
            })

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                          ["admin@kinangoptvc.ac.ke"], html_message=html)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, "contacts/send_success.html")

    else:
        form = contactForm()

    return render(request, 'contacts/contact.html', {'form': form})


def successView(request):
    return render(request, "contacts/send_success.html")

    # form = form.save()
    # return render(request, "contacts/send_success.html")
