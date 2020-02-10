from django.contrib.messages import constants as messages

AUTH_USER_MODEL = 'accounts.CustomUser'

MESSAGE_TAGS = {
    messages.ERROR:'alart alart-danger',
    messages.WARNING:'alert alert-warning',
    messages.SUCCESS:'alert alert-success',
    messages.INFO:'alert alert-info',
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'polls.apps.PollsConfig',
    'accounts.apps.AccountsConfig',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
]


SITE_ID = 1


AUTENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticalBackends',
    'django.contrib.auth.backends.ModelBackend',
)


ACCOUNT_AUTHENTICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True


LOGIN_REDIRECT_URL = 'diary:index'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'


ACCOUNT_LOGOUT_ON_GET = True