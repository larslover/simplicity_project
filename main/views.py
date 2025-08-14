from django.shortcuts import render



def home(request):
    return render(request, 'main/index.html')
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form to database
            form.save()

            # Prepare email data
            subject = f"New message from {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email'] or settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]

            # Send email safely
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    fail_silently=False,
                )
                email_sent = True
            except Exception as e:
                print("Email sending failed:", e)
                email_sent = False

            return render(
                request, 
                'main/contact.html', 
                {'form': ContactForm(), 'success': email_sent}
            )
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    return render(request, 'main/index.html')

def contact(request):
    email_sent = None  # Track if email was successfully sent

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # If ContactForm is NOT a ModelForm, remove this
            # form.save()

            # Prepare email data
            subject = f"New message from {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email'] or settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]

            # Try sending email
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    fail_silently=False,
                )
                email_sent = True
            except Exception as e:
                print("Email sending failed:", e)
                email_sent = False

            # Render form again (empty) after submission
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
