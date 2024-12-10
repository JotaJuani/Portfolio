from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('the form is valid')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']

            email_message = EmailMessage(
                subject=f'Contact Form from {name}',
                body=body,
                from_email=email,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],)
            email_message.send(fail_silently=False),
            form.save()
            messages.success(
                request, "Thank you for your message! I'll get back to you shortly.")

            return redirect('contact')
        else:
            messages.error(
                request, "There was an error with your submission. Please try again.")
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact_form.html', context)
