from __future__ import unicode_literals

from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from blog import signals

