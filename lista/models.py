from datetime import datetime
import uuid
from django.db import models


class tabela_cliente(models.Model):
    
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50) 
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nome



class tabela_produto (models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField( max_length=50)
    quantidade = models.CharField(max_length=50) 
    preco_unidade = models.CharField(("Preço_unidade $"),max_length=50)
    preco_total= models.CharField(("Preço_total $"),max_length=50)
   

    def __str__(self):
        return self.nome_produto



class tabela_venda(models.Model):
        
    tabela_id = models.ForeignKey(tabela_cliente, on_delete=models.CASCADE,blank=False)
    produto = models.ForeignKey(tabela_produto, on_delete=models.CASCADE,null=True)
    id_venda = uuid.uuid4()
    dia_venda = datetime.today()


def str(self):
    return self.id_venda 

class venda_possui_produto(models.Model):
    
    headline = models.CharField(max_length=100)
    list = models.ManyToManyField(tabela_venda)

    def __str__(self):
        return self.list