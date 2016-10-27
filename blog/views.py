from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LogIn


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