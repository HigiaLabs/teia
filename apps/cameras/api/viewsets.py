import base64
from io import BytesIO

import cv2
from PIL import Image
from apps.imagens.models import Imagens

try:
    from StringIO import StringIO  ## for Python 2
except ImportError:
    from io import StringIO  ## for Python 3
import numpy as np
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import CamerasSerializer


class CamerasViewSet(viewsets.ModelViewSet):
    serializer_class = CamerasSerializer
    queryset = Imagens.objects.all()


