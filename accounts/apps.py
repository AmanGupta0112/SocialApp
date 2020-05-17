from django.apps import AppConfig
# from __future__ import unicode_literals
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
