from rest_framework import serializers
from apps.imagens.models import Imagens


class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = '__all__'