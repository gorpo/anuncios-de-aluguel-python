from django.contrib.auth.models import User
from django.db import models

#MODEL DE IMOVEIS
class imoveis(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, null=False, blank=True)
    numero = models.CharField(max_length=5)
    cep = models.CharField(max_length=9)
    valor = models.CharField(max_length=8)
    descricao = models.TextField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(upload_to='alugue/media/imagens',  default='imagens/no-image.png', verbose_name='Imagem')
    created_at = models.DateTimeField('Criado em: ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em: ', auto_now=True)
    author = models.CharField(User, max_length=50)

    #RETORNAR NOME EM LISTAGEM
    def __str__(self):
        return self.nome






