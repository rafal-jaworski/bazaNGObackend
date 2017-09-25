from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager

KRS_FIELD_MAP = {
    'krs_podmioty.id': ('external_id', str),
    'krs_podmioty.nip': ('nip', str),
    'krs_podmioty.krs': ('krs', str),
    'krs_podmioty.nazwa': ('name', lambda x: dequote(str.title(x))),
    'krs_podmioty.cel_dzialania': ('purpose', str),
    'krs_podmioty.data_rejestracji': ('register_at', str),
    'krs_podmioty.nazwa_skrocona': ('short_name', lambda x: dequote(str.title(x))),
    'krs_podmioty.adres': ('address', str),
    'krs_podmioty.adres_kod_pocztowy': ('postal_code', str),
    'krs_podmioty.adres_ulica': ('street', str),
    'krs_podmioty.adres_numer': ('street_number', str),
    'krs_podmioty.adres_lokal': ('flat_number', str),
    'krs_podmioty.adres_miejscowosc': ('city', str),
    'krs_podmioty.adres_kraj': ('country', str),
}


def dequote(s):
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s


class Category(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255,)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return '{} ({})'.format(self.name, self.organizations.count())


class Person(models.Model):
    FIELD_MAP = {
        "nazwa": ("full_name", str),
        "data_urodzenia": ("date_of_birth", str),
        "osoba_id": ("external_id", str),
        "funkcja": ("position", str),
    }
    external_id = models.IntegerField(unique=True, verbose_name=_('ID in KRS database'))
    full_name = models.CharField(blank=True, max_length=255, verbose_name=_('full_name'))
    position = models.CharField(blank=True, max_length=255, verbose_name=_('position'))
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_('date of birth'))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')


class Organization(models.Model):
    LAYER_MAP = {
        'reprezentacja': 'administration',
        'nadzor': 'supervisory_authority',
    }
    external_id = models.IntegerField(blank=True, null=True, verbose_name=_('ID in KRS database'))
    nip = models.CharField(blank=True, max_length=255)
    krs = models.CharField(blank=True, max_length=255)
    external_department_number = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, verbose_name=_('Name'), max_length=255)
    short_name = models.CharField(blank=True, verbose_name=_('Short name'), max_length=255)
    purpose = models.TextField(blank=True, verbose_name=_('Purpose of the organization'))
    register_at = models.DateField(blank=True, null=True, verbose_name=_('Date of the registration'))
    address = models.CharField(blank=True, max_length=255)
    postal_code = models.CharField(blank=True, max_length=255)
    street = models.CharField(blank=True, max_length=255)
    street_number = models.CharField(blank=True, max_length=255)
    flat_number = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    country = models.CharField(blank=True, max_length=255)
    is_active = models.BooleanField(verbose_name=_('organization|is_active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='organizations')
    administration = models.ManyToManyField(Person, related_name='administers', verbose_name=_('organization|administration'))
    supervisory_authority = models.ManyToManyField(Person, related_name='supervise', verbose_name=_('organization|supervisory authority'))

    tags = TaggableManager()

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')
        ordering = ['name']
        indexes = []

    def __str__(self):
        return self.name


class OrganizationProfile(models.Model):
    name = models.CharField(blank=True, verbose_name=_('Name'), max_length=255)
    purpose = models.TextField(blank=True, verbose_name=_('Purpose of the organization'))
    organization = models.OneToOneField(Organization, related_name='profile')
    www = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(verbose_name=_("phone number"), blank=True, max_length=100)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = _('Organization profile')
        verbose_name_plural = _('Organization profiles')

    def __str__(self):
        return '{} profile'.format(self.organization.name)


class OrganizationProfileProposedChange(OrganizationProfile):
    profile = models.ForeignKey(OrganizationProfile, related_name='suggestions')

    class Meta:
        verbose_name = _('Organization profile proposed change')
        verbose_name_plural = _('Organization profile proposed changes')

    def __str__(self):
        return '{} proposed change'.format(self.profile)
