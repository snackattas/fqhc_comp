from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import UserProfile, Requirement

from functools import wraps
import logging

def requires_login(function):
    """This is a decorator that checks the request.user that is passed in by python social auth processes to confirm that python social auth worked.  If python social auth processes are not cleared, the decorator redirects to the login page."""

    @wraps(function)
    def decorated_function(*args, **kwargs):
        request = args[0]
        if not request.user or request.user.is_anonymous:
            return redirect('login')
        else:
            return function(*args, **kwargs)
    return decorated_function


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            error = True
            return render(request, 'login.html', {'error': error})
    if request.user:
        if request.user.is_authenticated():
            return redirect('dashboard')
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


@requires_login
def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'fqhc':user_profile.fqhc, 'requirements': Requirement.objects.all()})
