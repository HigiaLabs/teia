from django.db import models

# Criar o modelo aqui
from apps.cameras.models import Cameras


class Imagens(models.Model):
    imagem =  models.TextField()
    data = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    camera = models.ForeignKey(Cameras, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '__all__'

    def __repr__(self):
        return '__all__'

    class Meta():
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'