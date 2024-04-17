"""
Local Environment Settings
"""

from server.settings.components import BASE_DIR

SECRET_KEY = "django-insecure-+1!$%&^*()_+"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR.joinpath("staticfiles")

MEDIA_ROOT = BASE_DIR.joinpath("media")
