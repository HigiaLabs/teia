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

from .serializers import ImagensSerializer


class ImagensViewSet(viewsets.ModelViewSet):
    serializer_class = ImagensSerializer
    queryset = Imagens.objects.all()



    def create(self, request, *args, **kwargs):
        HAARCASCADE_FACE = 'apps/utils/haarcascade/haarcascade_frontalcatface.xml'
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        imagem = serializer.data.get('imagem')

        sbuf = BytesIO()
        sbuf.write(base64.b64decode(imagem))
        pimg = Image.open(sbuf)

        imagem = np.array(pimg)

        gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(HAARCASCADE_FACE)
        faces = face_cascade.detectMultiScale(gray, 1.3, 2)
        faces_detectadas =  list()
        for (x, y, w, h) in faces:
            cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)



        print(len(faces_detectadas))
        # cv2.imwrite("reconstructed.jpg", cv2_img)
        _, image_encode = cv2.imencode('.jpg', imagem)
        image_encode = base64.b64encode(image_encode).decode('utf8')

        return Response({"imagem_cinza": image_encode}, status=status.HTTP_200_OK)
