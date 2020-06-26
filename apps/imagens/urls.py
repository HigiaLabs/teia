from django.conf.urls import url
from django.urls import path
from . import views
from django.urls.conf import include
from django.urls import path
from django.contrib.auth.views import LoginView

from .api.viewsets import get_images, ocr_image
from .views import index

urlpatterns = [

    path('', index, name='index'),

    url(r'^imagens-tests', get_images, name='get_delete_update_puppy'),
    url(r'^imagens-ocr', ocr_image, name='ocr_image'),

]
