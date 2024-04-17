"""
Development Environment Settings
"""

from server.settings.components import config

SECRET_KEY = config("DJANGO_SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["*"]
