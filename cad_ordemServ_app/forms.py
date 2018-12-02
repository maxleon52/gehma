from django.forms import ModelForm
from .models import tb_os


class OsForm(ModelForm):
    class Meta:
        model = tb_os
        fields = ('defReclamado', 'defConstatado', 'ServRealizado', 'dataInicioOs', 'dataFinalOs', 'equipProxManu', 'tipo_serv', 'tipo_manut', 'tipo_aterramento', 'valor')
       # fields = '__all__'


class OsEditForm(ModelForm):
    class Meta:
        model = tb_os
        fields = ('defReclamado', 'defConstatado', 'ServRealizado', 'dataInicioOs',
                  'dataFinalOs', 'tipo_serv', 'tipo_manut', 'tipo_aterramento', 'cliCod', 'equipCod', 'valor')
       # fields = '__all__'
