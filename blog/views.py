from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LogIn, SignUp, PostAdd, PostEdit, TagAdd
from .models import Author, Post, Tag


def index(request):
    posts = Post.objects.order_by('redact_date')[::-1]
    users = Author.objects.all()
    tags = Tag.objects.all()
    try:
        user = Author.objects.get(is_loged=True)
        context = {'user': user, 'posts': posts,
                   'users': users, 'tags': tags}
        return render(request, 'index.html', context)
    except Author.DoesNotExist:
        context = {'posts': posts, 'users': users, 'tags': tags}
        return render(request, 'index.html', context)


def log_in(request):
        if request.method == 'POST':
            form = LogIn(request.POST)
            if 'submit' in request.POST:
                if form.is_valid():
                    try:
                        Author.objects.get(user_name=form.cleaned_data['user_name'],
                                           password=form.cleaned_data['password'])
                        user = Author.objects.get(user_name=form.cleaned_data['user_name'])
                        user.is_loged = True
                        user.save()
                        return HttpResponseRedirect('/blog/', {'user': user})
                    except Author.DoesNotExist:
                        return HttpResponseRedirect('/blog/log_in/')
            else:
                return render(request, 'index.html', {
                                'posts': Post.objects.order_by('redact_date')[::-1],
                                'users': Author.objects.all(),
                                'tags': Tag.objects.all()})
        else:
            form = LogIn()
        return render(request, 'login.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST, request.FILES)
        if 'submit' in request.POST:
            if form.is_valid():
                author = Author(user_name=form.cleaned_data['user_name'],
                                email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'],
                                reg_date=datetime.now(),
                                image=request.FILES.get('image', None))
                author.save()
                return HttpResponseRedirect('/blog/', {})
        else:
            return render(request, 'index.html', {
                'posts': Post.objects.order_by('redact_date')[::-1],
                'users': Author.objects.all(),
                'tags': Tag.objects.all()})
    else:
        form = SignUp()
    return render(request, 'sign_up.html', {'form': form})


def log_out(request):
    user = Author.objects.get(is_loged=True)
    user.is_loged = False
    user.save()
    return HttpResponseRedirect('/blog/', {})


def user_page(request):
    user = Author.objects.get(is_loged=True)
    posts = Post.objects.order_by('redact_date')[::-1]
    context = {'user': user, 'posts': posts}
    return render(request, 'user_page.html', context)


def post_page(request, pid):
    post = Post.objects.get(id=pid)
    post_author = Author.objects.get(user_name=post.author)
    tags = post.tag_set.all()
    try:
        user = Author.objects.get(is_loged=True)
        context = {'user': user, 'post': post,
                   'post_author': post_author,
                   'tags': tags}
        return render(request, 'post_page.html', context)
    except Author.DoesNotExist:
        context = {'post': post, 'post_author': post_author,
                   'tags': tags}
        return render(request, 'post_page.html', context)


def post_add(request):
    if request.method == 'POST':
        form = PostAdd(request.POST, request.FILES)
        if form.is_valid():
            user = Author.objects.get(is_loged=True)
            post = Post(author=Author.objects.get(user_name=user.user_name),
                        title=form.cleaned_data['title'],
                        text=form.cleaned_data['text'],
                        pub_date=datetime.now(),
                        redact_date=datetime.now(),
                        picture=request.FILES.get('picture', None))
            post.save()
            posts = Post.objects.order_by('redact_date')[::-1]
            context = {'user': user, 'posts': posts}
            return render(request, 'user_page.html', context)
    else:
        form = PostAdd()
    return render(request, 'post_add.html', {'form': form})


def post_edit(request, pid):
    post = Post.objects.get(id=pid)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        if request.FILES:
            post.picture = request.FILES.get('picture')
        post.redact_date = datetime.now()
        post.save()
        user = Author.objects.get(is_loged=True)
        context = {'user': user, 'post': post}
        return render(request, 'post_page.html', context)
    else:
        form = PostEdit(post=post)
    return render(request, 'post_edit.html', {'form': form})


def post_delete(request, pid):
    post = Post.objects.get(id=pid)
    post.delete()
    tags = Tag.objects.all()

    for tag in tags:
        if not tag.post.all():
            tag.delete()

    posts = Post.objects.order_by('redact_date')[::-1]
    user = Author.objects.get(is_loged=True)
    context = {'user': user, 'posts': posts}
    return render(request, 'user_page.html', context)


def tag_add(request, pid):
    if request.method == 'POST':
        form = TagAdd(request.POST)
        if form.is_valid():
            post = Post.objects.get(id=pid)
            tag = Tag(tag=form.cleaned_data['tag'])
            try:
                Tag.objects.get(tag=tag)
                tag = Tag.objects.get(tag=tag)
                tag.post.add(post)
                tag.save()
            except Tag.DoesNotExist:
                tag.save()
                tag.post.add(post)
                tag.save()

            tags = post.tag_set.all()
            user = Author.objects.get(is_loged=True)
            context = {'user': user, 'post': post, 'tags': tags}
            return HttpResponseRedirect('/blog/post_page/%s/' % pid, context)
    else:
        form = TagAdd()
    return render(request, 'tag_add.html', {'form': form})


def tag_posts(request, tid):
    tag = Tag.objects.get(id=tid)
    posts = tag.post.all()
    users = Author.objects.all()
    try:
        user = Author.objects.get(is_loged=True)
        context = {'posts': posts, 'tag': tag,
                   'user': user, 'users': users}
        return render(request, 'tag_posts.html', context)
    except Author.DoesNotExist:
        context = {'posts': posts, 'tag': tag, 'users': users}
        return render(request, 'tag_posts.html', context)


def test(request):
    return HttpResponse('link works')
