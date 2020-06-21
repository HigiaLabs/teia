from rest_framework import serializers
from ..models import Imagens


class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = '__all__'