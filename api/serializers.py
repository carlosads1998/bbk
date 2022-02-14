from dataclasses import fields
from rest_framework import serializers

from .models import Pedido, Avaliacao

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs={
            'email':{'write_only':True}
        }
        model = Pedido
        fields = (
            'item',
            'mesa',
            'email',
        )
        
class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = (
            'nome',
            'pedido',
            'nota',
        )