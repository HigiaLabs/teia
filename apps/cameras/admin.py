from django.contrib import admin

# Register your models here.
from apps.cameras.models import Cameras

admin.site.register(Cameras)