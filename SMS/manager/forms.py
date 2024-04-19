
# File Manualy created by Shivam

from django import forms
from .models import user_login_info

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Perform additional validation (e.g., username existence)
        # Raise a ValidationError if something's wrong

        return cleaned_data