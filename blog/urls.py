from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start/$', views.startPage, name='start'),
    url(r'^login/$', views.logIn, name='login'),
    url(r'^sign_up/$', views.signUp, name='sign_up'),
]