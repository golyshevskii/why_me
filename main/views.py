from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginpage')
def main_page(request):
    return render(request, 'main.html')
