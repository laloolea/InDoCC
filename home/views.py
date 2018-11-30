from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'home/index.html')

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home:index'))

    error = ""

    next = "/"

    if request.GET:
        next = request.GET['next']

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            error = "El nombre de usuario o la contraseña son errorneos."
        
    return render(request, 'home/login.html', {"login_error":error})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:login'))
