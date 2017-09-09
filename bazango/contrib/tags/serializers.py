from rest_framework import serializers
from taggit.models import Tag
from taggit_serializer.serializers import TaggitSerializer


class TagSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'