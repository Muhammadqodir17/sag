from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FooterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'footer'
    verbose_name = _('footer')
