"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.imagens.api.viewsets import ImagensViewSet
from apps.cameras.api.viewsets import CamerasViewSet

router = routers.DefaultRouter()

router.register(r'imagens', ImagensViewSet, basename='imagens')
router.register(r'cameras', CamerasViewSet, basename='cameras')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),

    path('', include('django.contrib.auth.urls')),
    path('', include(('apps.imagens.urls', 'images'), namespace='images')),
]
