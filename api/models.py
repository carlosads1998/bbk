import email
from django.db import models

class Base(models.Model):
    pedido = models.CharField(max_length=255)
    Avaliacao = models.CharField(max_length=255)
    
    class Meta:
        abstract = True


class Pedido (models.Model):
    item = models.CharField(max_length=255)
    mesa = models.DecimalField(max_digits=2, decimal_places=1)
    email = models.EmailField(blank=False)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    def __str__(self):
        return self.item

class Avaliacao(models.Model):
    nome = models.CharField(max_length=255)
    pedido = models.ForeignKey(Pedido, related_name='Avaliações', on_delete= models.CASCADE)
    nota = models.DecimalField(max_digits=3 ,decimal_places=1)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
    