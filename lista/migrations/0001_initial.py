# Generated by Django 3.2.9 on 2022-06-06 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tabela_cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tabela_produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=50)),
                ('quantidade', models.CharField(max_length=50)),
                ('preco_unidade', models.CharField(max_length=50, verbose_name='Preço_unidade $')),
                ('preco_total', models.CharField(max_length=50, verbose_name='Preço_total $')),
            ],
        ),
        migrations.CreateModel(
            name='tabela_venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lista.tabela_produto')),
                ('tabela_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lista.tabela_cliente')),
            ],
        ),
    ]
