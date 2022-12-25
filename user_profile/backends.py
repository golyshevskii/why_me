from django.contrib.auth.backends import ModelBackend
from .models import UserProfile


class UserAuthentication(ModelBackend):
    """User authentication by email or username"""

    def authenticate(self, request, username, password):
        if '@' in username:
            context = {'email': username}
        else:
            context = {'username': username}
        
        try:
            user = UserProfile.objects.get(**context)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            else:
                return None
        except UserProfile.DoesNotExist:
            return None
