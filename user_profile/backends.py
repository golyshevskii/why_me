from django.contrib.auth.backends import BaseBackend
from .models import UserProfile


class UserAuthentication(BaseBackend):
    """User authentication by email or username"""

    def authenticate(self, request, username, password):
        if '@' in username:
            context = {'email': username}
        else:
            context = {'username': username}
        
        try:
            user = UserProfile.objects.get(**context)
            if user.check_password(password):
                return user
            else:
                return None
        except UserProfile.DoesNotExist:
            return None
