# Generated by Django 2.2.13 on 2020-08-03 23:28

import cadastros.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('desconto', models.DecimalField(decimal_places=0, max_digits=3)),
                ('validade', models.DateField(null=True, verbose_name='data de validade')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FormaEnvio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('estoque', models.IntegerField()),
                ('valorVenda', models.DecimalField(decimal_places=2, max_digits=50)),
                ('imagem', models.ImageField(blank=True, max_length=255, null=True, upload_to='imagens/%Y/%m/%d/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_venda', models.DateTimeField(auto_now=True)),
                ('desconto', models.CharField(blank=True, max_length=100, null=True, verbose_name='cupom de desconto')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('parcelas', models.CharField(choices=[('1', 'À Vista'), ('2', '2x'), ('3', '3x')], max_length=100)),
                ('forma_envio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.FormaEnvio')),
                ('forma_pagamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.FormaPagamento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ProdutoVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('qtde', models.IntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Venda')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Digite seu nome completo', max_length=50, null=True, verbose_name='Qual seu nome?')),
                ('nascimento', models.DateField(null=True, verbose_name='data de nascimento')),
                ('endereco', models.CharField(max_length=100, null=True)),
                ('numero', models.CharField(max_length=10, null=True, verbose_name='Número')),
                ('cep', models.CharField(max_length=25, null=True)),
                ('rg', models.CharField(max_length=25, null=True)),
                ('cpf', models.CharField(max_length=25, null=True, validators=[cadastros.models.validate_CPF])),
                ('telefone', models.CharField(max_length=25, null=True)),
                ('cidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.Cidade')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parcela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_parcela', models.IntegerField()),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=50)),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Venda')),
            ],
        ),
        migrations.CreateModel(
            name='EntradaProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=0, max_digits=8)),
                ('data_entrada', models.DateTimeField(auto_now=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Produto')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Estado'),
        ),
    ]
