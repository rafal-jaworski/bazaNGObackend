from rest_framework import serializers
from .models import Organization, OrganizationProfile
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)


class OrganizationProfileSerializer(TaggitSerializer, serializers.ModelSerializer):

    class Meta:
        model = OrganizationProfile
        exclude = ('organization',)


class OrganizationSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    profile = OrganizationProfileSerializer(read_only=True)

    class Meta:
        model = Organization
        fields = '__all__'

