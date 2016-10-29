from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.logIn, name='login'),
    url(r'^sign_up/$', views.signUp, name='sign_up'),
    # url(r'^user_profile/$', views.user_profile, name='user_profile'),
    url(r'^user_profile_(?P<user_id>[0-9]+)/$', views.user_profile, name='user_profile'),
]