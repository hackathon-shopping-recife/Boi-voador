from django.db import models
# Create your models here.

class cliente(models.Model):
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=30)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    id_comprador = models.IntegerField(default=0)



class compra(models.Model): # TODO: show list of products and descriptions too
    id_compra = models.IntegerField(default=0)
    id_comprador = models.IntegerField(default=0)
    cnpj = models.CharField(max_length=20)
    valor = models.IntegerField(default=0) # TODO: change to float
    qnt_itens = models.IntegerField(default=0) 
    data_emissao = models.DateTimeField('date published')
    # TODO: Add link field
