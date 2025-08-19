from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    def clean_honeypot(self):
        data = self.cleaned_data['honeypot']
        if data:  # if a bot filled it
            raise forms.ValidationError("Spam detected.")
        return data
