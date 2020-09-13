from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        # The user has info and wants and account now
        if request.POST['password'] == request.POST['confirmpassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(
                    request,
                    'accounts/signup.html',
                    {'error': 'Username has already been taken'}
                )
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password']
                )
                auth.login(request, user)
                return redirect('home')
        else:
            return render(
                request,
                'accounts/signup.html',
                {'error': 'Passwords must match! Try Again.'}
            )
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')
