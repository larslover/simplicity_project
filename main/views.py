from django.shortcuts import render



def home(request):
    return render(request, 'main/index.html')
from django.shortcuts import render, redirect
from .forms import ContactForm
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
            print("Sending email to console:", form.cleaned_data)


            # Send email
            send_mail(
                subject=f"New message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=[settings.EMAIL_HOST_USER],  # your business email
                fail_silently=False,
            )
            print("Email should have been printed to console backend")

            return render(request, 'main/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
