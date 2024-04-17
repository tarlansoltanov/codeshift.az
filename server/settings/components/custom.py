# Custom Project Settings

from server.settings.components import BASE_DIR
from server.settings.components.common import INSTALLED_APPS, TEMPLATES

# Application definition

INSTALLED_APPS += [
    "server.apps.base",
    "server.apps.portfolio",
]

# Context processors
# https://docs.djangoproject.com/en/5.0/ref/templates/api/#writing-your-own-context-processors

TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    "server.apps.base.context_processors.contact_details",
    "server.apps.portfolio.context_processors.categories",
]

# Static and media files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/topics/files/

STATICFILES_DIRS = [
    BASE_DIR.joinpath("static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
