from rest_framework import generics

from .models import Pedido, Avaliacao
from .serializers import PedidoSerializer,AvaliacaoSerializer

class PedidosAPIView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class= PedidoSerializer
    
class PedidoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class= PedidoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer