from django.db import models

# Create your models here.
from datetime import datetime
import uuid
from django.db import models


class tabela_cliente(models.Model):

    id_cliente = uuid.uuid4()
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
    id_produto = uuid.uuid4()
    nome_produto = models.CharField( max_length=50)
    quantidade = models.CharField(max_length=50) 
    preco_unidade = models.CharField(("Preço_unidade $"),max_length=50)
    preco_total= models.CharField(("Preço_total $"),max_length=50)


    def str(self):
        return self.nome_produto



class tabela_venda(models.Model):

    tabela_id = models.ForeignKey(tabela_cliente, on_delete=models.CASCADE,blank=False)
    produto = models.ForeignKey(tabela_produto, on_delete=models.CASCADE,null=True)
    id_venda = uuid.uuid4()
    dia_venda = datetime.now()


def str(self):
    return self.id_venda