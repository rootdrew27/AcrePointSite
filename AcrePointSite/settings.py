from pathlib import Path
import os
from EnvVarReader.env_var_reader import Secrets

secrets = Secrets("ENV_VARS.json")


# For Production
# -------------------
# Set DEBUG to False 
# Set database (migrate if necessary)
# Adjust the settings at the bottom of this file 
# -------------------
DEBUG = True

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = secrets.getSecret("SECRET_KEY")

INSTALLED_APPS = [
    'LandingPage',
    'Gallery',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'AcrePointSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
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

WSGI_APPLICATION = 'AcrePointSite.wsgi.application' 

import dj_database_url

DATABASES = {
    # Settings to use with a Connection String
    # 'default': {
    #     dj_database_url.config(
    #         default=dj_database_url.parse(os.environ.get("DATABASE_URL")),
    #         conn_max_age=600
    #     )
    # }

        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': secrets.getSecret("DATABASE_NAME"),
        'USER': secrets.getSecret("DATABASE_USERNAME"),
        'PASSWORD': secrets.getSecret("DATABASE_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'application_name': "AcrePointSite" #this is displayed in pgAdmin
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_ENGINE = "django.contrib.sessions.backends.file"

SESSION_FILE_PATH = os.path.join(BASE_DIR, 'SessionFiles')

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# SETTINGS for Production
if (DEBUG == False):

    ALLOWED_HOSTS = []

    STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

    # STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" # Depreciated in Django 4.2

    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

    CSRF_COOKIE_SECURE = True

    SESSION_COOKIE_SECURE = True

