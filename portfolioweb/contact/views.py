
from django.shortcuts import render, redirect
from .models import Contact
from .forms import  ContactForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,)
        if form.is_valid():
            print('the form is valid')
            name = request.cleaned_data['name']
            email = request.cleaned_data['email']
            body = request.cleaned_data['body']

            email_message = EmailMessage(
                subject=f'Contact Form from {name}',
                body=body,
                from_email=email,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],)
            email_message.send(fail_silently=False),
            form.save()
            messages.success(
                request, "Thank you for your message! We'll get back to you shortly.")
            print(email)
            return render(request, 'base/home.html')
    else:
        form = ContactForm()

    context = {'form': form, }
    return render(request, 'base/home.html', context)

