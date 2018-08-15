# Create your models here.
from django.db import models

class tb_clientes(models.Model):  # CRIA A TABELA COM SEUS RESPECTIVOS CAMPOS

    nome = models.CharField(max_length=200)
    nomeFant = models.CharField(max_length=200)
    cep = models.CharField(max_length=8, null='True', blank='True')
    endereco = models.CharField(max_length=100, null='True', blank='True')
    bairro = models.CharField(max_length=50, null='True', blank='True')
    cidade = models.CharField(max_length=100, null='True', blank='True')
    uf = models.CharField(max_length=2)
    cnpj = models.CharField(max_length=14)
    cpf = models.CharField(max_length=12)
    contato = models.CharField(max_length=50, null='True', blank='True')
    email = models.CharField(max_length=50, null='True', blank='True')
    tel = models.CharField(max_length=11, null='True', blank='True')
    cel1 = models.CharField(max_length=11, null='True', blank='True')
    cel2 = models.CharField(max_length=11, null='True', blank='True')
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome