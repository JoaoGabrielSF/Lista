# Generated by Django 4.0.2 on 2022-02-17 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0004_remove_tabela_venda_tabela_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabela_venda',
            name='teste',
            field=models.CharField(default=6, max_length=50),
        ),
        migrations.AlterField(
            model_name='tabela_venda',
            name='tabela_nome',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lista.tabela_cliente'),
        ),
    ]
