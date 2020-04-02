# Generated by Django 2.1.7 on 2020-04-02 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0008_remove_venda_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='email',
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cep',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.Cidade'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='endereco',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(null=True, verbose_name='data de nascimento'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(help_text='Digite seu nome completo', max_length=50, null=True, verbose_name='Qual seu nome?'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='numero',
            field=models.CharField(max_length=10, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='rg',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
