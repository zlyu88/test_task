from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^$', views.index, name='log_out'),
    url(r'^post_add/$', views.post_add, name='post_add'),
    url(r'^post_page/$', views.post_page, name='post_page'),


    # url(r'^user_profile/$', views.user_profile, name='user_profile'),
    # url(r'^user_(?P<user_id>[0-9]+)/$', views.user_, name='user_'),

    url(r'^post_add/$', views.post_add, name='post_add'),
    url(r'^user_page/$', views.user_page, name='user_page'),
]