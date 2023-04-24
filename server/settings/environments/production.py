"""
Production Environment Settings
"""

from server.settings.components import config
from server.settings.components.database import DATABASES

SECRET_KEY = config("DJANGO_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = []

ALLOWED_HOSTS.extend(config('DOMAIN_NAMES', cast=lambda v: [s.strip() for s in v.split(',')]) or [])
ALLOWED_HOSTS.extend(config('DOMAIN_IPS', cast=lambda v: [s.strip() for s in v.split(',')]) or [])

DATABASES['default']['CONN_MAX_AGE'] = 500

# CSRF settings

CSRF_TRUSTED_ORIGINS = []

CSRF_TRUSTED_ORIGINS.extend(config('DOMAIN_NAMES', cast=lambda v: [f"http://{s.strip()}" for s in v.split(',')]) or [])
CSRF_TRUSTED_ORIGINS.extend(config('DOMAIN_IPS', cast=lambda v: [f"http://{s.strip()}" for s in v.split(',')]) or [])