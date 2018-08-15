from django.db import models

class tb_equip(models.Model):

    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50, null='True', blank='True')
    marca = models.CharField(max_length=50, null='True', blank='True')
    tensao = models.CharField(max_length=6, null='True', blank='True')
    proxManu = models.DateField()
    numSerie = models.CharField(max_length=20, null='True', blank='True')
    fotoFrente = models.ImageField(upload_to='Fotos_Equip', null='True', blank='True')
    fotoVerso = models.ImageField(upload_to='Fotos_Equip', null='True', blank='True')

    def __str__(self):
        return self.nome + ' ' + self.modelo + ' ' + self.marca