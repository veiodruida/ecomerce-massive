# Django settings for massivecoupon project.
import socket, os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
FORCE_SCRIPT_NAME = ''
DEFAULT_CITY_SLUG = 'goiania'

# Site-based configuration parameters
_host = socket.gethostname().lower()

#informacoes sistema
AUTH_PROFILE_MODULE = 'accounts.userprofile'
SITE_NAME = 'Clipper Magazine Brasil'
META_KEYWORDS = 'Descontos, Cupons, Gratuito,Compra,Coletiva'
META_DESCRIPTION = 'Site de compras coletivas'
SESSION_COOKIE_AGE = 7776000 # the number of seconds in 90 days
LOGIN_REDIRECT_URL = '/'

PHOTOLOGUE_DIR = 'ofertas'

SECRET_KEY = ''

FACEBOOK_API_KEY = ''
FACEBOOK_SECRET_KEY = ''
SOCIAL_GENERATE_USERNAME = True

PAYPAL_USER  = ""
PAYPAL_PASSWORD = ""
PAYPAL_SIGNATURE = ""
PAYPAL_DEBUG = True

ADMINS = (
  ('Jhoni', 'veiodruida@gmail.com'),
  ('Miltinho Brandao', 'miltinho@gmail.com'),
  ('Marinho Brandao', 'marinho@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'massive001',
        'USER': 'postgres',
        'PASSWORD': '1234',
    }
}


#SESSION_COOKIE_DOMAIN = '.massivecoupon.com'
#GOOGLE_MAPS_API_KEY = '' # in last API version, API is not anymore necessary


TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

try:
    from local_settings import *
except ImportError:
    pass

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH, 'estatico')
STATIC_URL = '/estatico/'

ADMIN_MEDIA_PREFIX = '/admin-media/'



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    #'engine.tcp.cities',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'massivecoupon.thread_locals.ThreadLocals',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    #'facebook.djangofb.FacebookMiddleware',
    #'socialregistration.middleware.FacebookMiddleware'
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # this is the default backend, don't forget to include it!
    'massive.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    # this is what you're adding for using Twitter
#    'massivecoupon.socialregistration.auth.TwitterAuth',
    #'massivecoupon.socialregistration.auth.FacebookAuth', # Facebook
#    'massivecoupon.socialregistration.auth.OpenIDAuth', # OpenID
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT_PATH,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'tagging',
    'south',
    'massive.engine',
    #'massive001.countries',
    #'massive001.photologue',
    #'massive001.socialregistration', 
   # 'massive001.paypalxpress',
#    'debug_toolbar',    
)

LOGIN_URL = "/usuario/login/"
LOGIN_REDIRECT_URL = "/"

