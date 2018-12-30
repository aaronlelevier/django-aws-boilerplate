from .prod import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'user',
        'PASSWORD': 'password',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
