from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.apps.app_payments'
    verbose_name = 'Payment'
    verbose_name_plural = 'Payments'

    def ready(self):
        import src.apps.app_payments.signals
