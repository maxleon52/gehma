from django.db import models
from cad_clientes_app.models import tb_clientes

class tb_equip(models.Model):
    cod = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    modelo = models.CharField('Modelo', max_length=50, null='True', blank='True')
    cliCod = models.ForeignKey(tb_clientes, null=True, blank=True, on_delete=models.SET_NULL)
    marca = models.CharField(max_length=50, null='True', blank='True')
    tensao = models.CharField('Tensão',max_length=6, null='True', blank='True')
    proxManu = models.DateField('Próxima Manutenção')
    numSerie = models.CharField('Número de Série',max_length=20, null='True', blank='True')
    fotoFrente = models.ImageField(upload_to='Fotos_Equip', null='True', blank='True')
    fotoVerso = models.ImageField(upload_to='Fotos_Equip', null='True', blank='True')

    def __str__(self):
        return str(self.nome) + ' ' + str(self.modelo) + ' ' + str(self.marca)


class tb_orcamentos(models.Model):
    nomeEquip = models.CharField(max_length=20)
    qtd = models.CharField(max_length=8)
    valorUnit = models.CharField(max_length=8)

    #def __str__(self):
     #   return self.nomeEquip + ' '+ str(self.qtd) + str(self.valorUnit)