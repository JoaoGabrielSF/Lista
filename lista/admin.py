from django.contrib import admin
from lista.models import tabela_cliente, tabela_produto, tabela_venda 

class Clientes(admin.ModelAdmin):
    list_display = ('id_cliente', 'nome', 'cpf', 'telefone','endereco', 'bairro' , 'cidade', 'estado')
    list_display_links =('id_cliente', 'nome')
    search_fields = ('id_client', 'name')

admin.site.register(tabela_cliente,Clientes)

class Produtos(admin.ModelAdmin):
    list_display = ('id_produto', 'nome_produto', 'quantidade','preco_unidade', 'preco_total')
    list_display_links =('id_produto', 'nome_produto')
    search_fields = ('id_produto', 'nome_produto')

admin.site.register(tabela_produto,Produtos)


class Vendas(admin.ModelAdmin):
    list_display = ('id_venda','id_cliente', 'dia_venda')
    list_display_links =('id_venda','dia_venda')
    search_fields = ('id_venda','id_cliente', 'dia_venda')

admin.site.register(tabela_venda,Vendas)