from django.db import models

# Create your models here.
class NovaModel(models.Model):
    nome = Models.charField(max_lengt=45)

def __str__(self) -> str:
    return self.nome 