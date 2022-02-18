from datetime import datetime
import uuid
from django.db import models
from django.forms import CharField
from django.test import client


class tabela_cliente(models.Model):
    
    id_cliente = uuid.uuid1()
    nome = models.CharField(max_length=50) 
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def str(self):
        return self.nome



class tabela_produto (models.Model):
    id_produto = uuid.uuid1()
    nome_produto = models.CharField( max_length=50)
    quantidade = models.CharField(max_length=50) 
    preco_unidade = models.CharField(("Preço_unidade $"),max_length=50)
    preco_total= models.CharField(("Preço_total $"),max_length=50)
   

def str(self):
    return self.nome_produto , self.id_produto



class tabela_venda(models.Model):
        
        id_nome = models.ForeignKey(tabela_cliente, on_delete=models.CASCADE)
        id_venda = uuid.uuid1()
        dia_venda = datetime.today()
        

def str(self):
    return self.id_venda , self.dia_venda


#class venda_possui_produto(models.Model):
#   pass