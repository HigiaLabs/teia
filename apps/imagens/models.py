from django.db import models

# Criar o modelo aqui

class Imagens(models.Model):
    imagem =  models.TextField()
    data = models.DateTimeField(auto_created=True, blank=True,null=True)