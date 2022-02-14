from unicodedata import name
from django.urls import path

from .views import PedidoAPIView,PedidosAPIView, AvaliacaoAPIView, AvaliacoesAPIView

urlpatterns = [
    path('pedidos/', PedidosAPIView.as_view(), name = 'Pedidos'),
    path('avaliacao/', AvaliacoesAPIView.as_view(), name = 'Avaliações'),
    path('pedidos/<int:pk>/', PedidoAPIView.as_view(), name = 'Pedido'),
    path('avaliacao/<int:pk>/', AvaliacaoAPIView.as_view, name = "Avaliação"),
]
