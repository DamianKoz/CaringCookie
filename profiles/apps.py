from django.apps import AppConfig
from django.apps import apps as django_apps


class RegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
