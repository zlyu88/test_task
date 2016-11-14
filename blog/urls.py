from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^log_out/$', views.log_out, name='log_out'),

    url(r'^user_page/$', views.user_page, name='user_page'),

    url(r'^post_add/$', views.post_add, name='post_add'),
    url(r'^post_page/(?P<pid>\d+)/$', views.post_page, name='post_page'),
    url(r'^post_edit/(?P<pid>\d+)/$', views.post_edit, name='post_edit'),
    url(r'^post_delete/(?P<pid>\d+)/$', views.post_delete, name='post_delete'),

    url(r'^tag_add/(?P<pid>\d+)/$', views.tag_add, name='tag_add'),
    url(r'^tag_posts/(?P<tid>\d+)/$', views.tag_posts, name='tag_posts'),


    url(r'^test/$', views.test, name='test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)