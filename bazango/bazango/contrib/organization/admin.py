from django.contrib import admin
from .models import Organization, OrganizationProfile
# Register your models here.


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(OrganizationProfile)
class OrganizationProfileAdmin(admin.ModelAdmin):
    pass
