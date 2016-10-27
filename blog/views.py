from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LogIn, SignUp


def index(request):
    return HttpResponse('Hello, world. You\'re at the blog index!!!')

def startPage(request):
    return HttpResponse('Log in or sign up')

def logIn(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = LogIn()
    return render(request, 'login.html', {'form': form})

def signUp(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = SignUp()
    return render(request, 'sign_up.html', {'form': form})