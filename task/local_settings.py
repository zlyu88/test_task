import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'user',
        'PASSWORD': '1234',
        'NAME': 'blog',
    }
}

DEBUG = True
