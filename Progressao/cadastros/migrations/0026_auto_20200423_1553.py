# Generated by Django 2.2.10 on 2020-04-23 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0025_auto_20200423_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'ordering': ['-pk']},
        ),
    ]