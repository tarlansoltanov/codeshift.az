from django.utils.translation import gettext_lazy as _

from server.settings.components.common import MIDDLEWARE
from server.settings.components import BASE_DIR

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

MIDDLEWARE.insert(2, 'django.middleware.locale.LocaleMiddleware')

LANGUAGE_CODE = 'az'

LANGUAGES = (
   ('az', _('Azerbaijani')),
   ('en', _('English')),
   ('ru', _('Russian')),
)

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
   BASE_DIR.joinpath('locale'),
]