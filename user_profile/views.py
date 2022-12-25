from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from . import forms



@login_required(login_url='loginpage')
def user_profile_page(request, user=None):
    """Function that render user profile page"""
    context = {'user': user}
    return render(request, template_name='user_profile.html', context=context)

@login_required(login_url='loginpage')
def to_user_profile_page(request):
    """Function that redirect user to the user profile page"""

    return redirect('userprofilepage', user=request.user.username)


class LoginPage(LoginView):
    """Class that login a user into site"""

    form_class = forms.LoginForm
    template_name = 'login.html'


@login_required(login_url='loginpage')
def logout_page(request):
    logout(request)
    return redirect('loginpage')
