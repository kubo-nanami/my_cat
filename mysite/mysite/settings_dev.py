from .settings_common import *
import os

#SECURITY WARNING: donc't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#ロギング設定
LOGGING = {
    'version': 1, #固定
    'disable_existing_loggers': False,

    #ロガーの設定
    'loggers':{
        #Djangoが利用するロガー
        'django':{
            'handlers':['console'],
            'level':'INFO', 
        },
        #pollsが利用するロガー
        'diary':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },

    #ハンドラの設定
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    #フォーマッタの設定
    'formatters':{
        'dev':{
            'format':'/t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(Lineno)d)',
                '%(message)s'
            ])
        }
    }
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'piw36sk4n0@^(k1w6&d=2g3%=u3@ragv3o-4t!r^rsr23s@g=='