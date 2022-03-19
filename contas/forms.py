from django.forms import ModelForm
from .models import Pedido,Cliente

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

