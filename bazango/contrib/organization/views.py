import pyexcel
from rest_framework import viewsets, views, parsers, response, status

from bazango.contrib.organization.filters import OrganizationFilterSet
from .models import Organization, Category, OrganizationProfileProposedChange
from .serializers import (OrganizationSerializer, CategorySerializer, OrganizationProfileProposedChangeSerializer)


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


class OrganizationProfileProposedChangeViewSet(viewsets.ModelViewSet):
    queryset = OrganizationProfileProposedChange.objects.all()
    serializer_class = OrganizationProfileProposedChangeSerializer


class FileUploadView(views.APIView):
    parser_classes = (parsers.FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        file_obj.save_to_database(Organization)
        return response.Response(status=201)
