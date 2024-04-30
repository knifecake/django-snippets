import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'test-key'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'tests',
    'shortuuid',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test',
    }
}
