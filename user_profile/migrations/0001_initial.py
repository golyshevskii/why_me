# Generated by Django 4.1.4 on 2022-12-22 16:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=170, verbose_name='Country')),
                ('code', models.CharField(max_length=10, verbose_name='Country code')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Contries',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=170, verbose_name='City')),
                ('slug', models.SlugField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.country', verbose_name='Country of the city')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='User email')),
                ('password', models.CharField(max_length=64, verbose_name='User password')),
                ('is_active', models.BooleanField(default=True, verbose_name='User is active')),
                ('is_stuff', models.BooleanField(default=False, verbose_name='User is stuff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='User is admin')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('fullname', models.CharField(max_length=255, verbose_name='Full name')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('country', models.CharField(max_length=170, verbose_name='Country of residence')),
                ('city', models.CharField(max_length=170, verbose_name='City of residence')),
                ('phone', models.CharField(max_length=20, verbose_name='User phone number')),
                ('site', models.CharField(max_length=255, verbose_name='User site')),
                ('photo', models.ImageField(upload_to='images/photos/', verbose_name='User photo')),
                ('cover', models.ImageField(upload_to='images/covers/', verbose_name='User cover')),
                ('general_info', models.TextField(max_length=2000, verbose_name='User general information')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
