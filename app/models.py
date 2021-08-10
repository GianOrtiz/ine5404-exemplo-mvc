from django.db import models
from django.urls import reverse

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=128)
    codigo = models.CharField(max_length=64)
    valor = models.FloatField()
    quantidade = models.IntegerField()

    def get_absolute_url(self):
        return reverse('products-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{0} - {1} | R$ {2} | Quantidade: {3}'.format(
            self.codigo, self.nome, self.valor, self.quantidade)

    def __repr__(self):
        return self.__str__()
