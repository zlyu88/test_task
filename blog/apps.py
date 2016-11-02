from __future__ import unicode_literals

from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from blog import signals
<<<<<<< HEAD

=======
>>>>>>> 4e6d4b6b6ba00630ed7df82a6b542a3c9de17484
