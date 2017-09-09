from rest_framework import viewsets

from bazango.contrib.organization.filters import OrganizationFilterSet
from .models import Organization, Category
from .serializers import OrganizationSerializer, CategorySerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    search_fields = ('name', 'address', 'krs')
    filter_class = OrganizationFilterSet
    ordering_fields = ('name',)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


