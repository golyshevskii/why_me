from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile


class LoginForm(AuthenticationForm):
    """Form for login process"""

    class Meta:
        model = UserProfile
        fields = ['username', 'password']
