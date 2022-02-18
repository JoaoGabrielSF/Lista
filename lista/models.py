from datetime import datetime
import uuid
from django.db import models
from django.test import client


class tabela_cliente(models.Model):
    
<<<<<<< HEAD
    id_cliente = uuid.uuid1()
=======
    id_cliente = uuid.uuid4()
>>>>>>> 5d338b37e7cdc450b4e93f30e42731d0f44bc2eb
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
<<<<<<< HEAD
    id_produto = uuid.uuid1()
=======
    id_produto = uuid.uuid4()
>>>>>>> 5d338b37e7cdc450b4e93f30e42731d0f44bc2eb
    nome_produto = models.CharField( max_length=50)
    quantidade = models.CharField(max_length=50) 
    preco_unidade = models.CharField(("Preço_unidade $"),max_length=50)
    preco_total= models.CharField(("Preço_total $"),max_length=50)
   

def str(self):
    return self.nome_produto , self.id_produto



class tabela_venda(models.Model):
        
<<<<<<< HEAD
        id_nome = models.ForeignKey(tabela_cliente, on_delete=models.CASCADE)
        id_venda = uuid.uuid1()
        dia_venda = datetime.today()
        
=======
    tabela_id = models.ForeignKey(tabela_cliente, on_delete=models.CASCADE,blank=False)
    id_venda = uuid.uuid4()
    dia_venda = datetime.today()

>>>>>>> 5d338b37e7cdc450b4e93f30e42731d0f44bc2eb

def str(self):
    return self.id_venda , self.dia_venda


