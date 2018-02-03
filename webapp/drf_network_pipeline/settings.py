"""
Django settings for drf_network_pipeline project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""
import os
from configurations import Configuration
from configurations import values


class Common(Configuration):

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
        "0.0.0.0",
        "zap"
    ]

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.sites',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',

        'rest_framework',
        'rest_framework_swagger',
        'rest_framework.authtoken',
        'rest_registration',
        'rest_framework_jwt',
        'django_extensions',
        'debug_toolbar',

        'drf_network_pipeline.users',
        'drf_network_pipeline.pipeline',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'drf_network_pipeline.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'drf_network_pipeline.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases  # noqa E501
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )

    # Password validation
    # https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#auth-password-validators # noqa
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
        },
    ]

    SITE_ID = 1

    # Internationalization
    # https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # noqa

    AUTH_USER_MODEL = 'users.User'

    # https://github.com/szopu/django-rest-registration#configuration
    REST_REGISTRATION = {
        'REGISTER_VERIFICATION_ENABLED': False,
        'RESET_PASSWORD_VERIFICATION_URL': '/reset-password/',
        'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
        'VERIFICATION_FROM_EMAIL': 'no-reply@example.com',
    }

    # http://getblimp.github.io/django-rest-framework-jwt/
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.AllowAny',
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
    }

    # http://getblimp.github.io/django-rest-framework-jwt/
    """

    One of these is breaking the api-token-auth - 2018-02-02

    JWT_AUTH = {
        'JWT_ENCODE_HANDLER':
        'rest_framework_jwt.utils.jwt_encode_handler',
        'JWT_DECODE_HANDLER':
        'rest_framework_jwt.utils.jwt_decode_handler',
        'JWT_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_payload_handler',
        'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
        'JWT_RESPONSE_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_response_payload_handler',
        'JWT_SECRET_KEY': SECRET_KEY,
        'JWT_GET_USER_SECRET_KEY': None,
        'JWT_PUBLIC_KEY': None,
        'JWT_PRIVATE_KEY': None,
        'JWT_ALGORITHM': 'HS256',
        'JWT_VERIFY': True,
        'JWT_VERIFY_EXPIRATION': True,
        'JWT_LEEWAY': 0,
        'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
        'JWT_AUDIENCE': None,
        'JWT_ISSUER': None,
        'JWT_ALLOW_REFRESH': False,
        'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
        'JWT_AUTH_HEADER_PREFIX': 'JWT',
        'JWT_AUTH_COOKIE': None,
    }
    """
# end of Common


class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
        "0.0.0.0",
        "zap"
    ]

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]


class Staging(Common):
    """
    The in-staging settings.
    """
    # Security
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    SECURE_REDIRECT_EXEMPT = values.ListValue([])
    SECURE_SSL_HOST = values.Value(None)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    SECURE_PROXY_SSL_HEADER = values.TupleValue(
        ('HTTP_X_FORWARDED_PROTO', 'https')
    )


class Production(Staging):
    """
    The in-production settings.
    """
    pass