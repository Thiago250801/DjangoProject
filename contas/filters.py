import django_filters
from django_filters import DateFilter
from .models import *

class PedidoFilter(django_filters.FilterSet):


    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ['data_publicacao']