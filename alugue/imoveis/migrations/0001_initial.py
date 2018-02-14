# Generated by Django 2.0.2 on 2018-02-14 01:39

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imoveis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('complemento', models.CharField(blank=True, max_length=100)),
                ('numero', models.CharField(max_length=5)),
                ('cep', models.CharField(max_length=9)),
                ('valor', models.CharField(max_length=8)),
                ('descricao', models.TextField()),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(default='imagens/no-image.png', upload_to='alugue/media/imagens', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em: ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em: ')),
                ('author', models.CharField(max_length=50, verbose_name=django.contrib.auth.models.User)),
            ],
        ),
    ]
