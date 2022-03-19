from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('produtos/', views.produtos, name = "produtos"),
    path('cliente/<str:pk_test>/', views.cliente, name= "cliente"),
    path('gerar_pedido/', views.gerarPedido, name= "gerar_pedido"),
    path('cadastrar_cliente/', views.cadastrarCliente, name= "cadastrar_cliente"),
    path('atualizar_pedido/<str:pk>/', views.atualizarPedido, name= "atualizar_pedido"),
    path('remover_pedido/<str:pk>/', views.removerPedido, name="remover_pedido"),
]
