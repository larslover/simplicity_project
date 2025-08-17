from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def home(request):
    return render(request, 'main/index.html')
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import logging

# Set up a simple logger
logger = logging.getLogger(__name__)

def contact(request):
    email_sent = None
    error = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            # Validate email
            try:
                validate_email(email)
            except ValidationError:
                error = "Please enter a valid email address."
                # Log the attempt with name and message, but no email
                logger.warning(f"Contact form submitted without valid email. Name: {form.cleaned_data.get('name')}, Message: {form.cleaned_data.get('message')}")
                return render(request, 'main/contact.html', {
                    'form': form,
                    'success': False,
                    'error': error
                })

            # Save valid submission
            form.save()

            # Send email
            subject = f"New message from {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            from_email = email
            recipient_list = [settings.EMAIL_HOST_USER]

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                email_sent = True
            except Exception as e:
                print("Email sending failed:", e)
                email_sent = False

            return render(request, 'main/contact.html', {
                'form': ContactForm(),
                'success': email_sent
            })
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {
        'form': form,
        'success': email_sent
    })
