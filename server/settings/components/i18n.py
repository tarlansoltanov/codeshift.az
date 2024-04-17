from django.utils.translation import gettext_lazy as _

from server.settings.components import BASE_DIR
from server.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

MIDDLEWARE.insert(2, "django.middleware.locale.LocaleMiddleware")

LANGUAGE_CODE = "az"

LANGUAGES = (
    ("az", _("Azerbaijani")),
    ("en", _("English")),
    ("ru", _("Russian")),
)

TIME_ZONE = "Asia/Baku"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR.joinpath("locale"),
]

# Rosetta Configuration
# For detailed information, see documentation :
# https://django-rosetta.readthedocs.io/

INSTALLED_APPS.insert(0, "rosetta")

ROSETTA_AUTO_COMPILE = True

ROSETTA_SHOW_AT_ADMIN_PANEL = True

ROSETTA_WSGI_AUTO_RELOAD = True

ROSETTA_UWSGI_AUTO_RELOAD = True

# Modeltranslation Configuration
# For detailed information, see documentation :
# https://django-rosetta.readthedocs.io/

INSTALLED_APPS.insert(0, "modeltranslation")
