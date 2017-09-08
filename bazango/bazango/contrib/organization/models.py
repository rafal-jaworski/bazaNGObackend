from django.db import models
from django.utils.translation import ugettext as _

KRS_FIELD_MAP = {
    'id': 'external_id',
    'nip': 'nip',
    'nazwa': 'name',
    'cel_dzialania': 'purpose',
    'data_rejestracji': 'register_at',
    'nazwa_skrocona': 'short_name',
    'adres': 'full_address',
    'adres_kod_pocztowy': 'postal_code',
    'adres_ulica': 'street',
    'adres_numer': 'street_number',
    'adres_lokal': 'flat_number',
    'adres_miejscowosc': 'city',
    'adres_kraj': 'country',
}


class Organization(models.Model):
    # USABLE
    external_id = models.IntegerField(_('ID in KRS database'))
    nip = models.IntegerField()
    name = models.CharField(_('Name'), max_length=255)
    short_name = models.CharField(_('Short name'), max_length=255)
    purpose = models.TextField(_('Purpose of the organization'))
    register_at = models.DateField(_('Date of the registration'))
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    flat_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')
        ordering = ['name']
        indexes = []


# class OrganizationProfile(models.Model):
#     organization = models.OneToOneField(Organization)


