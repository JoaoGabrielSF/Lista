import random
from django.db import models
from django.test import client


class tabela_cliente(models.Model):
    
    id_cliente = random.sample(range(0,100000), 1)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

def str(self):
        return self.nome, self.id_cliente



class tabela_produto (models.Model):
    id_produto = random.sample(range(0,100000),1)
    nome_produto = models.CharField( max_length=50)
    quantidade = models.CharField(max_length=50) 
    preco_unidade = models.CharField(("Preço_unidade $"),max_length=50)
    preco_total= models.CharField(("Preço_total $"),max_length=50)
   

def str(self):
    return self.nome_produto , self.id_produto



class tabela_venda(models.Model):
    
        id_venda = random.sample(range(0,100000),1)
        id_cliente = tabela_cliente.id_cliente
        dia_venda = models.CharField(max_length=14, unique=True)

def str(self):
    return self.id_venda , self.dia_venda