from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Country(models.Model):
    """Counrty model"""

    country = models.CharField(verbose_name='Country', max_length=170)
    code = models.CharField(verbose_name='Country code', max_length=10)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Contries'

    def __str__(self):
        return self.country


class City(models.Model):
    """City model"""

    city = models.CharField(verbose_name='City', max_length=170)
    country = models.ForeignKey(Country, verbose_name='Country of the city', on_delete=models.CASCADE)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city


class UserProfileManager(BaseUserManager):
    """Manager for the new user creation"""

    def _create_user(self, email, password=None):
        if not email:
            raise ValueError('The user email must be set')
        
        email = self.normalize_email(email=email)
        user = self.model(email=email)
        user.password = make_password(password)
        
        # save into default DB
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self._create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """User profile model"""

    username = models.CharField(verbose_name='Username', max_length=100, unique=True)
    email = models.EmailField(verbose_name='User email', max_length=255, unique=True, blank=False, null=False)
    password = models.CharField(verbose_name='User password', max_length=256)
    is_active = models.BooleanField(verbose_name='User is active', default=True)
    is_staff = models.BooleanField(verbose_name='User is stuff', default=False)
    is_superuser = models.BooleanField(verbose_name='User is admin', default=False)
    date_joined = models.DateTimeField(verbose_name="Date joined", default=timezone.now)

    fullname = models.CharField(verbose_name='Full name', max_length=255, blank=True, null=True)
    birthday = models.DateField(verbose_name='Birthday', blank=True, null=True)
    country = models.CharField(verbose_name='Country of residence', max_length=170, blank=True, null=True)
    city = models.CharField(verbose_name='City of residence', max_length=170, blank=True, null=True)
    phone = models.CharField(verbose_name='User phone number', max_length=20, blank=True, null=True)
    site = models.CharField(verbose_name='User site', max_length=255, blank=True, null=True)

    photo = models.ImageField(verbose_name='User photo', upload_to='images/photos/', blank=True, null=True)
    cover = models.ImageField(verbose_name='User cover', upload_to='images/covers/', blank=True, null=True)
    general_info = models.TextField(verbose_name='User general information', max_length=2000, blank=True, null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self) -> str:
        return self.email
