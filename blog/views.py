from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NameForm


def index(request):
    return HttpResponse('Hello, world. You\'re at the blog index!!!')

def startPage(request):
    return HttpResponse('Log in or sign up')