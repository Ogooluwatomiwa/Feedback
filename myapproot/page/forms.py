from django import forms
from .models import Page
from django.core.validators import EmailValidator
import re

class PageForm(forms.ModelForm):
    forenames = forms.CharField()
    lastname  = forms.CharField()
    email     = forms.EmailField() #validators=[EmailValidator()])
    feedback  = forms.Textarea()
    class Meta:
        model = Page
        fields = [
            'forenames',
            'lastname',
            'email',
            'feedback',
        ]

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if "com" not in email:
    #         raise forms.ValidationError('Enter a valid email')
    #     if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
    #         raise forms.ValidationError('Enter a valid email')
    #     return email
