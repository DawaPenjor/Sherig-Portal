from django.apps import AppConfig


class SherigappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SherigApp'

    def ready(self):
        import SherigApp.signals
