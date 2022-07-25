from .base import *

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prode_info_new',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}