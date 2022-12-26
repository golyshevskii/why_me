from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate


@login_required(login_url='loginpage')
def user_profile_page(request, username=None):
    """Function that render user profile page"""
    return render(request, 'user_profile.html')


@login_required(login_url='loginpage')
def to_user_profile_page(request):
    """Function that redirect user to the user profile page"""

    return redirect('userprofilepage', username=request.user.username)


def login_page(request):
    context = {'error': None}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, 
                            username=username, 
                            password=password)

        if user:
            login(request, user)
            return redirect('userprofilepage', username=user.username)
        else:
            context['error'] = 'incorrect username or password'

    return render(request, 'login.html', context=context)



@login_required(login_url='loginpage')
def logout_page(request):
    logout(request)
    return redirect('loginpage')
