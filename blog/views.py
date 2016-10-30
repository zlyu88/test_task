from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LogIn, SignUp, PostAdd
from .models import Author, Post


def index(request):
    return render(request, 'index_main.html',
                  {'posts': Post.objects.all()})


def log_in(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            try:
                Author.objects.get(user_name=form.cleaned_data['user_name'],
                                   password=form.cleaned_data['password'])
                user = Author.objects.get(user_name=form.cleaned_data['user_name'])
                return render(request, 'index_main.html', {'user': user.user_name,
                                                           'posts': Post.objects.all(),
                                                           'login':True})
                # return HttpResponseRedirect('/blog/', {'user': user.user_name,'login':True})
            except Author.DoesNotExist:
                return HttpResponseRedirect('/blog/log_in/')
    else:
        form = LogIn()
    return render(request, 'login.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST, request.FILES)
        if form.is_valid():
            author = Author(user_name=form.cleaned_data['user_name'],
                            email=form.cleaned_data['email'],
                            password=form.cleaned_data['password'],
                            reg_date=datetime.now(),
                            picture=form.cleaned_data['picture'])
            author.save()
            user = author.user_name
            # return HttpResponseRedirect('/blog/user_%s/' % user_id)
            # return render(request, '/blog/user_%s/' % user_id, {'login':True})
            return render(request, 'index_main.html', {'user': user,
                                                       'posts': Post.objects.all(),
                                                       'login': True})
    else:
        form = SignUp()
    return render(request, 'sign_up.html', {'form': form})


# def log_out(request):
#     return redirect('index')


def user_page(request, user):
    # user = Author.objects.get(id=user_id)
    # name = user.user_name
    # picture = user.picture
    # return HttpResponse('User profile %s.' % name)
    return render(request, 'user_page.html', {'name': user})


def post_add(request, user='Oleg'):
    if request.method == 'POST':
        form = PostAdd(request.POST, request.FILES)
        if form.is_valid():
            post = Post(author=Author.objects.get(user_name=user),
                        title=form.cleaned_data['title'],
                        text=form.cleaned_data['text'],
                        pub_date=datetime.now(),
                        redact_date=datetime.now(),
                        picture=form.cleaned_data['picture'])
            post.save()
            return HttpResponse('sucsess!')
            # return render(request, 'user_page.html', {'user': user,
            #                                           'posts': Post.objects.all(),
            #                                           'login': True})
    else:
        form = PostAdd()
    return render(request, 'post_add.html', {'form': form})


def post_page(request, title='some'):
    post = Post.objects.get(title=title)
    return render(request, 'post_page.html', {'post': post})


# def post_add(request):
#     return HttpResponse('post_add form here')

#
# def user_page(request):
#     return render(request, 'user_page.html', {})