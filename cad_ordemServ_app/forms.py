from django.forms import ModelForm
from .models import tb_os


class OsForm(ModelForm):
    class Meta:
        model = tb_os
        fields = ('cod', 'defReclamado', 'defConstatado', 'ServRealizado', 'dataInicioOs', 'dataFinalOs', 'cliCod', 'equipCod', 'tipo_serv', 'tipo_manut', 'tipo_aterramento')
       # fields = '__all__'
