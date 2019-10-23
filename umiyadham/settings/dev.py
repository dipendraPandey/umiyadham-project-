from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=2_deiijtms-4vxet+_ru7amfhy6w$_o$5x1htjrxfr)*16i-o'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

# ########################### The following code for enabling  django-debug-toolbar ######@@dipendra###############
INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    # #### following app is to enable the style guide in cma ########### @@dipendra
    'wagtail.contrib.styleguide',
]
MIDDLEWARE = MIDDLEWARE + [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
# ######################################## Toolbar code ends here ##########@@dipendra##############################

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
