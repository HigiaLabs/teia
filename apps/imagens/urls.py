from django.urls import path
from . import views
from django.urls.conf import include
from django.urls import path
from django.contrib.auth.views import LoginView

from .views import index

urlpatterns = [

    path('', index, name='index'),

]
