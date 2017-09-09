from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OrganizationConfig(AppConfig):
    name = 'bazango.contrib.organization'
    verbose_name = _('Organization')

    def ready(self):
        import bazango.contrib.organization.signals
