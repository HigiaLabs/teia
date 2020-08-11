import base64
from io import BytesIO

import cv2
from PIL import Image
from apps.imagens.models import Imagens
from rest_framework.decorators import action, api_view

from ...utils.processing.face_detect import Face

try:
    from StringIO import StringIO  ## for Python 2
except ImportError:
    from io import StringIO  ## for Python 3
import numpy as np
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ImagensSerializer
import cv2
import pytesseract


class ImagensViewSet(viewsets.ModelViewSet):
    serializer_class = ImagensSerializer



    @action(methods=['get'], detail=True)
    def get_queryset(self):
        return Imagens.objects.all()

    # @action(methods=['post'], detail=True)
    def create(self, request, *args, **kwargs):
        face = Face()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        imagem = serializer.data.get('imagem')
        sbuf = BytesIO()
        sbuf.write(base64.b64decode(imagem))
        pimg = Image.open(sbuf)
        imagem = np.array(pimg)
        imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)
        num, data = face.detect(imagem)


        return Response({"imagem_cinza": data  }, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)
    def ocr_camera(self, request, pk=None):
        return "Rota Funcionando"


@api_view(['GET'])
def get_images(request):
    try:
        queryset = Imagens.objects.all()
    except Imagens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({})


@api_view(['GET', 'POST'])
def ocr_image(request):
    # get all puppies
    if request.method == 'GET':

        imPath = 'apps\\utils\\images\\modelo_cupom_fiscal.png'
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        config = ('-l eng --oem 1 --psm 3')
        # Read image from disk
        im = cv2.imread(imPath, cv2.IMREAD_COLOR)
        # Run tesseract OCR on image
        text = pytesseract.image_to_string(im, config=config)
        # Print recognized text
        # print(text)
        return Response({'tetse': text})



    # insert a new record for a puppy
    elif request.method == 'POST':
        imPath = 'apps\\utils\\images\\modelo_cupom_fiscal.png'
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        config = ('-l eng --oem 1 --psm 3')
        # Read image from disk
        im = cv2.imread(imPath, cv2.IMREAD_COLOR)
        # Run tesseract OCR on image
        text = pytesseract.image_to_string(im, config=config)
        # Print recognized text
        # print(text)

        return Response({'tetse': text})
