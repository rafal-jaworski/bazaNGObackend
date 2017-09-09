from django.contrib import admin
from .models import Organization, OrganizationProfile, Category, Person
from django.utils.translation import ugettext_lazy as _


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'krs', 'register_at', 'tag_list', 'category_list', 'is_active']
    actions = ['make_active', 'make_inactive']
    search_fields = ['name', 'address', 'krs']
    list_filter = ['is_active', 'tags', 'categories', 'register_at']
    preserve_filters = True

    def get_queryset(self, request):
        return super(OrganizationAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def category_list(self, obj):
        return u", ".join(o.name for o in obj.categories.all())

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = _('Mark selected organizations as active')

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = _('Mark selected organizations as inactive')


@admin.register(OrganizationProfile)
class OrganizationProfileAdmin(admin.ModelAdmin):
    # list_display = ['organization__short_name', 'organization__krs', 'organization__register_at',
    #                 'organization__tag_list', 'organization__is_active']
    # search_fields = ['organization__name', 'organization__address']
    pass


class CategoriesInline(admin.TabularInline):
    model = Organization.categories.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoriesInline
    ]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
