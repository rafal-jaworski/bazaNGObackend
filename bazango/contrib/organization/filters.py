import django_filters

from bazango.contrib.organization.models import Organization


class OrganizationFilterSet(django_filters.FilterSet):
    class Meta:
        model = Organization
        fields = {
            'name': ['exact', 'contains'],
            'tags__name': ['in'],
            'categories__name': ['in'],
        }
