from django.db import models

class tb_equip(models.Model):
    cod = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50, null='True', blank='True')
    marca = models.CharField(max_length=50, null='True', blank='True')
    tensao = models.CharField(max_length=6, null='True', blank='True')
    proxManu = models.DateField()
    numSerie = models.CharField(max_length=20, null='True', blank='True')
    fotoFrente = models.ImageField(upload_to='Fotos_Equip', null='True', blank='True')
    fotoVerso = models.ImageField(upload_to='Fotos_Equip', null='True', blank='True')

    def __str__(self):
        return str(self.nome) + ' ' + str(self.modelo) + ' ' + str(self.marca)


class tb_orcamentos(models.Model):
    nomeEquip = models.CharField(max_length=20)
    qtd = models.CharField(max_length=8)
    valorUnit = models.CharField(max_length=8)

    def __str__(self):
        return self.nomeEquip + ' '+ str(self.qtd) + str(self.valorUnit)