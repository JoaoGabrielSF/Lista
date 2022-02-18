from dataclasses import fields
from rest_framework import serializers
from lista.models import tabela_cliente,tabela_produto,tabela_venda

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = tabela_cliente
        Fields = ['id_cliente','nome','cpf','telefone','endereco','bairro', 'cidade', 'estado']
        

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tabela_produto
        Fields = ['id_produto', 'nome_produto', 'quantidade','preco_unidade', 'preco_total']
        

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tabela_venda
        Fields = ['tabela_nome','id_venda','dia_venda']