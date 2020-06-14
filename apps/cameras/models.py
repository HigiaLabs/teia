from django.db import models

# Create your models here.

class Cameras(models.Model):
    host= models.CharField(max_length=300, blank=True, null=True)
    area_de_interesse = models.CharField(max_length=300, blank=True, null=True)
    nome_camera = models.CharField(max_length=300, blank=True, null=True)
    localizacao_fisica = models.CharField(max_length=300, blank=True, null=True)


    def __str__(self):
        return '__all__'

    def __repr__(self):
        return '__all__'

    class Meta():
        verbose_name = 'Camera'
        verbose_name_plural = 'Cameras'