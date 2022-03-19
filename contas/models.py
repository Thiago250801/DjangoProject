from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True)
    telefone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    data_pubicacao = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    CATEGORIA = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    nome = models.CharField(max_length=200, null=True)
    preco = models.FloatField(null=True)
    categoria = models.CharField(max_length=200, null=True, choices=CATEGORIA)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.nome
class Pedido(models.Model):
    STATUS = (
        ('Pendente','Pendente'),
        ('Saiu pra entrega','Saiu pra entrega'),
        ('Entregue','Entregue'),
    )
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    produto = models.ForeignKey(Produto, null=True, on_delete=models.SET_NULL)
    data_publicacao = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.produto.nome
