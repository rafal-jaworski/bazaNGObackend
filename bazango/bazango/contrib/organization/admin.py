from django.contrib import admin
from .models import Organization, OrganizationProfile
from django.utils.translation import ugettext_lazy as _


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'krs', 'register_at', 'tag_list', 'is_active']
    actions = ['make_active', 'make_inactive']

    def get_queryset(self, request):
        return super(OrganizationAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = _('Mark selected organizations as active')

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = _('Mark selected organizations as inactive')


@admin.register(OrganizationProfile)
class OrganizationProfileAdmin(admin.ModelAdmin):
    pass
