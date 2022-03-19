clientes = Cliente.objects.all()

primeiroCliente = CLiente.objects.first()

ultimoCLiente = Cliente.objects.last()

clientePorNome = Cliente.objects.get(name='Paulo')

clientePorId = Cliente.objects.get(id=4)

primeiroCliente.pedido_set.all()

pedido = Pedido.objects.first()
parentNome = pedido.cliente.nome

produtos = Produto.objects.filter(category="Out Door")

leastToGreatest = Produto.objects.all().order_by('id')
greatestToLeast = Produto.objects.all().order_by('-id')


produtosFiltered = Produto.objects.filter(tags__name="Sports")


ballOrders = primeiroCliente.order_set.filter(produto__nome="Ball").count()

allPedidos = {}

for pedido in primeiroCliente.pedido_set.all():
	if pedido.product.name in allPedidos:
		allPedidos[pedido.produto.nome] += 1
	else:
		allPedidos[pedido.produto.nome] = 1



class ParentModel(models.Model):
	nome = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Cliente)
	nome = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
parent.childmodel_set.all()
