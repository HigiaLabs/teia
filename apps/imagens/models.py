from django.db import models

# Criar o modelo aqui

class Imagens(models.Model):
    imagem =  models.TextField()
    data = models.DateTimeField(auto_created=True, blank=True,null=True)

    def __str__(self):
        return '__all__'

    def __repr__(self):
        return '__all__'

    class Meta():
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'