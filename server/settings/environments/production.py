"""
Production Environment Settings
"""

from server.settings.components import config
from server.settings.components.database import DATABASES

SECRET_KEY = config("DJANGO_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    config("DOMAIN_NAME"), 
    config("DOMAIN_IP"), 
    f'www.{config("DOMAIN_NAME")}', 
    'web'
]

DATABASES['default']['CONN_MAX_AGE'] = 500

# CSRF settings

CSRF_TRUSTED_ORIGINS = [
    f'http://{config("DOMAIN_NAME")}', 
    f'http://www.{config("DOMAIN_NAME")}', 
    f'http://{config("DOMAIN_IP")}', 
    'http://web'
]