from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
<<<<<<< HEAD
    url(r'^log_out/$', views.log_out, name='log_out'),
    # url(r'^post_page(?P<user_id>[0-9]+)/$', views.post_page, name='post_page'),
    url(r'^post_page/(?P<pid>\d+)/$', views.post_page, name='post_page'),
    url(r'^post_delete/(?P<pid>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^test/$', views.test, name='test'),

    url(r'^post_edit/(?P<pid>\d+)/$', views.post_edit, name='post_edit'),
    url(r'^tag_add/(?P<pid>\d+)/$', views.tag_add, name='tag_add'),
    url(r'^tag_posts/(?P<tid>\d+)/$', views.tag_posts, name='tag_posts'),
=======
    url(r'^$', views.index, name='log_out'),
    url(r'^post_add/$', views.post_add, name='post_add'),
    url(r'^post_page/$', views.post_page, name='post_page'),


>>>>>>> 4e6d4b6b6ba00630ed7df82a6b542a3c9de17484
    # url(r'^user_profile/$', views.user_profile, name='user_profile'),
    # url(r'^user_(?P<user_id>[0-9]+)/$', views.user_, name='user_'),

    url(r'^post_add/$', views.post_add, name='post_add'),
    url(r'^user_page/$', views.user_page, name='user_page'),
]