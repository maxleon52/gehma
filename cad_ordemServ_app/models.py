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
    defReclamado = models.CharField(max_length=200)
    defConstatado = models.CharField(max_length=200)
    ServRealizado = models.CharField(max_length=200)
    dataOs = models.DateField(auto_now_add=True)  # ESTA DATA NÃO ESTÁ APARECENDO NO ADMIN, ESTÁ OCULTA
    dataInicioOs = models.DateField(auto_now_add=False)
    dataFinalOs = models.DateField(auto_now_add=False)
    cliCod = models.ForeignKey(tb_clientes, null=True, blank=True, on_delete=models.SET_NULL)
    equipCod = models.ForeignKey(tb_equip, null=True, blank=True, on_delete=models.SET_NULL)
    tipo_serv = models.CharField(max_length=8, choices=TIPO_SERV)
    tipo_manut = models.CharField(max_length=10, choices=TIPO_MANUT)
    tipo_aterramento = models.CharField(max_length=3, choices=TIPO_ATERRAMENTO)

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
        return str(self.data) + self.histReclamado + self.hConstatado + self.hServRealizado + str(self.hEquipCod)
