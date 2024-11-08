INSTALLED_APPS = [
    ...
    'chartapp',
    'rest_framework',
    'django_nvd3',
    ...
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoproject',
        'USER': 'postgres',  # Use an existing role here
        'PASSWORD': 'test123',  # Replace with the actual password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# TEMPLATE_DIRS = (
#     os.path.join(SETTINGS_PATH, 'templates'),
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


# import os
# from pathlib import Path

# # Base directory
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Secret Key (for development only)
# SECRET_KEY = 'your-secret-key-for-local-development'

# # Debug mode
# DEBUG = True

# # Allowed Hosts
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# # Installed Apps
# INSTALLED_APPS = [
#     # Default Django apps
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     # Third-party apps
#     'crispy_forms',
#     'crispy_bootstrap5',
#     'rest_framework',
#     'django_extensions',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',

#     # Your custom apps
#     'chartapp',  # Replace with your app names
# ]

# # Middleware
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# # Root URL configuration
# ROOT_URLCONF = 'djangoproject.urls'

# # Templates
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# # WSGI Application
# WSGI_APPLICATION = 'djangoproject.wsgi.application'

# # Database (PostgreSQL)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'djangoproject',  # Change to your local database name
#         'USER': 'postgres',       # Change to your local database user
#         'PASSWORD': 'password',   # Change to your local database password
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# # Language and time zone
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True

# # Static files
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']

# # Media files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# # Crispy Forms
# CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5