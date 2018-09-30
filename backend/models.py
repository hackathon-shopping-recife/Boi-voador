from django.db import models
# Create your models here.

class cliente(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    senha = models.CharField(max_length=30)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    id_comprador = models.IntegerField(default=0)



class compra(models.Model): # TODO: show list of products and descriptions too
    id_comprador = models.IntegerField(default=0)
    cnpj = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    qnt_itens = models.IntegerField(default=0) 
    data_emissao = models.DateTimeField('date published')
    url = models.CharField(max_length=500, unique=True)

class item(models.Model):
    descricao = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    compra = models.ForeignKey(compra, on_delete=models.CASCADE)