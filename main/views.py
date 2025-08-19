from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
import logging

# Set up a simple logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'main/index.html')
def contact(request):
    email_sent = None
    error = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Honeypot check: if a bot filled it, just discard silently
            if form.cleaned_data.get('honeypot'):
                # Pretend success so bot doesn't try again
                return render(request, 'main/contact.html', {
                    'form': ContactForm(),
                    'success': True
                })

            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            # Validate email
            try:
                validate_email(email)
            except ValidationError:
                error = "Please enter a valid email address."
                logger.warning(f"Contact form submitted without valid email. Name: {name}, Message: {message}")
                return render(request, 'main/contact.html', {
                    'form': form,
                    'success': False,
                    'error': error
                })

            # Save valid submission
            form.save()

            # Prepare email
            subject = f"New message from {name}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]

            email_message = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=recipient_list,
                reply_to=[email]
            )

            # Send email
            try:
                email_message.send(fail_silently=False)
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
