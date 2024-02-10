"""
Production Environment Settings
"""

from server.settings.components import config
from server.settings.components.database import DATABASES

SECRET_KEY = config("DJANGO_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [f'*.{config("DOMAIN_NAME")}', config("DOMAIN_IP"), "web"]

DATABASES["default"]["CONN_MAX_AGE"] = 500

# CSRF settings

CSRF_TRUSTED_ORIGINS = [
    f'https://{config("DOMAIN_NAME")}',
    f'https://{config("DOMAIN_IP")}',
    "https://codeshift.az",
    "http://web",
]
