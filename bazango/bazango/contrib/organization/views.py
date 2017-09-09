from rest_framework import viewsets

from bazango.contrib.organization.filters import OrganizationFilterSet
from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    search_fields = ('name', 'address')
    filter_class = OrganizationFilterSet
    ordering_fields = ('name',)

