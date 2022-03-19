from django.shortcuts import render, redirect
from .forms import PedidoForm,ClienteForm
# Create your views here.
from .models import *
from .filters import PedidoFilter

def home(request):
    pedido = Pedido.objects.all()
    clientes = Cliente.objects.all()

    total_clientes = clientes.count()
    total_pedidos = pedido.count()
    entregue = pedido.filter(status ='Entregue').count()
    pendente = pedido.filter(status = 'Pendente').count()

    context = {'pedido':pedido,'clientes':clientes,
               'total_pedidos':total_pedidos,'entregue':entregue,
               'pendente':pendente}

    return render(request, 'contas/dashboard.html', context)

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'contas/produtos.html', {'produtos':produtos})

def cliente(request, pk_test):
    cliente = Cliente.objects.get(id=pk_test)

    pedido = cliente.pedido_set.all()
    pedido_count = pedido.count()

    meuFilter = PedidoFilter(request.GET, queryset=pedido)
    pedido = meuFilter.qs

    context = {'cliente':cliente, 'pedido':pedido, 'pedido_count':pedido_count, 'meuFilter':meuFilter}
    return render(request, 'contas/cliente.html', context)

def gerarPedido(request):
    form = PedidoForm()
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'contas/pedido_form.html', context)

def cadastrarCliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'contas/cadastrar_form.html', context)


def atualizarPedido(request, pk):


    pedido = Pedido.objects.get(id=pk)
    form = PedidoForm(instance = pedido)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance = pedido)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'contas/pedido_form.html', context)


def removerPedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    if request.method == "POST":
        pedido.delete()
        return redirect('/')
    context = {'item':pedido}
    return render(request, 'contas/remover.html', context)