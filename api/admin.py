from django.contrib import admin

from .models import Pedido, Avaliacao

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('item', 'mesa', 'email')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pedido', 'nota')