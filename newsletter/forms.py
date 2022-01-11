from django import forms
from .models import Newsletter

class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        
        widgets = {
                'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'max-length':'64',
                    }),
                }
