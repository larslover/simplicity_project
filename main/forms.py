from django import forms
from .models import ContactMessage
# forms.py
import random, string
import time
def random_field_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

class ContactForm(forms.ModelForm):
    timestamp = forms.FloatField(widget=forms.HiddenInput, initial=time.time)
    honeypot_name = random_field_name()
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label=honeypot_name)

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'honeypot']

    def clean(self):
        cleaned_data = super().clean()
        honeypot = cleaned_data.get('honeypot')
        form_time = cleaned_data.get('timestamp')
        if honeypot:
            raise forms.ValidationError("Spam detected.")
        if form_time and (time.time() - form_time) < 3:
            raise forms.ValidationError("Spam detected: submitted too fast.")
        return cleaned_data
