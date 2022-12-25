from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    """Form for login process"""

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    error_messages = {
        "invalid_login": "Please enter a correct login data",
        "inactive": "This account is inactive",
    }
