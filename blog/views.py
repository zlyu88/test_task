from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LogIn, SignUp
from .models import Author


def index(request):
    return render(request, 'index.html', {})


def logIn(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/user_profile/')
    else:
        form = LogIn()
    return render(request, 'login.html', {'form': form})


def signUp(request):
    if request.method == 'POST':
        form = SignUp(request.POST, request.FILES)
        if form.is_valid():
            author = Author(user_name=form.cleaned_data['user_name'],
                            email=form.cleaned_data['email'],
                            password=form.cleaned_data['password'],
                            reg_date=datetime.now(),
                            picture=form.cleaned_data['picture'])
            author.save()
            user_id = author.id
            return HttpResponseRedirect('/blog/user_profile_%s/' % user_id)
    else:
        form = SignUp()
    return render(request, 'sign_up.html', {'form': form})


# def user_profile(request, user_id):
#     return HttpResponse('User profile {}',format(user_id))

def user_profile(request, user_id):
    user = Author.objects.get(id=user_id)
    name = user.user_name
    picture = user.picture
    return HttpResponse('User profile %s.' % name)