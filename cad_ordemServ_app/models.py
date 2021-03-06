from django.db import models
from django.db.models import PROTECT, CASCADE
from django.utils.datetime_safe import datetime

from cad_clientes_app.models import tb_clientes
from cad_equip_app.models import tb_equip


# Create your models here.

class tb_os(models.Model):
    TIPO_SERV = (
        ('contrato', 'CONTRATO'),
        ('garantia', 'GARANTIA'),
        ('avulso', 'AVULSO'),
    )
    TIPO_MANUT = (
        ('corretiva', 'CORRETIVA'),
        ('preventiva', 'PREVENTIVA'),
    )
    TIPO_ATERRAMENTO = (
        ('sim', 'SIM'),
        ('nao', 'NÃO'),
    )
    cod = models.AutoField(primary_key=True)
    defReclamado = models.CharField("DEFEITO RECLAMADO",max_length=200)
    defConstatado = models.CharField("DEFEITO CONSTATADO",max_length=200)
    ServRealizado = models.CharField("SERVIÇO REALIZADO",max_length=200)
    dataOs = models.DateField(auto_now_add=True)  # ESTA DATA NÃO ESTÁ APARECENDO NO ADMIN, ESTÁ OCULTA
    dataInicioOs = models.DateField("DATA INICIAL",auto_now_add=False)
    dataFinalOs = models.DateField("DATA FINAL",auto_now_add=False)
    cliCod = models.ForeignKey(tb_clientes, null=True, blank=True, on_delete=models.SET_NULL)
    cliNome = models.CharField(max_length=200, null='True', blank='True')
    cliCnpj = models.CharField(max_length=14, null='True', blank='True')
    cliCpf = models.CharField(max_length=12, null='True', blank='True')
    cliContato = models.CharField(max_length=50, null='True', blank='True')
    cliCep = models.CharField(max_length=8, null='True', blank='True')
    cliEndereco = models.CharField(max_length=100, null='True', blank='True')
    cliBairro = models.CharField(max_length=50, null='True', blank='True')
    cliCidade = models.CharField(max_length=100, null='True', blank='True')
    cliUf = models.CharField(max_length=2, null='True', blank='True' )
    equipCod = models.ForeignKey(tb_equip, null=True, blank=True, on_delete=models.SET_NULL)
    tipo_serv = models.CharField("SERVIÇO",max_length=8, choices=TIPO_SERV)
    tipo_manut = models.CharField("MANUTENÇÃO",max_length=10, choices=TIPO_MANUT)
    tipo_aterramento = models.CharField("ATERRAMENTO", max_length=3, choices=TIPO_ATERRAMENTO)
    status = models.CharField("STATUS", max_length=10, null='True', blank='True')
    equipProxManu = models.DateField("PROX. MANUTENÇÃO", auto_now_add=False)
    valor = models.DecimalField("VALOR", max_digits=9   , decimal_places=2)

    def __str__(self):
        return 'Nº O.S.: ' + str(self.cod) + ' -- ' + str(self.tipo_serv)


class tb_historico(models.Model):
    data = models.DateField(default=datetime.now)
    histReclamado = models.CharField(max_length=200)
    hConstatado = models.CharField(max_length=200)
    hServRealizado = models.CharField(max_length=200)
    hEquipCod = models.ForeignKey(tb_equip, null=True, blank=True, on_delete=models.SET_NULL)
    hOsCod = models.ForeignKey(tb_os, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.data) + str(self.histReclamado) + str(self.hConstatado) + str(self.hServRealizado) + str(self.hEquipCod)
