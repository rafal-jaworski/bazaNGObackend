"""bazango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .contrib.organization.views import (OrganizationViewSet, CategoryViewSet, OrganizationProfileProposedChangeViewSet,
                                         FileUploadView)
from .contrib.tags.views import TagViewSet


router = DefaultRouter()
router.register(r'organization', OrganizationViewSet)
router.register(r'tag', TagViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'category-proposal', OrganizationProfileProposedChangeViewSet)


api_urlpatterns = [
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include(router.urls)),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urlpatterns)),
    url(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())
]


