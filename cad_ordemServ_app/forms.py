from django.forms import ModelForm, DateInput
from .models import tb_os


class DateInputCustom(DateInput):
    input_type = 'date'


class OsForm(ModelForm):
    class Meta:
        model = tb_os
        fields = (
        'defReclamado', 'defConstatado', 'ServRealizado', 'dataInicioOs', 'dataFinalOs', 'equipProxManu', 'tipo_serv',
        'tipo_manut', 'tipo_aterramento', 'valor')
        widgets = {
            'dataInicioOs': DateInputCustom(format='%Y-%m-%d'),
            'dataFinalOs': DateInputCustom(format='%Y-%m-%d'),
        }


class OsEditForm(ModelForm):
    class Meta:
        model = tb_os
        fields = ('defReclamado', 'defConstatado', 'ServRealizado', 'dataInicioOs',
                  'dataFinalOs', 'tipo_serv', 'tipo_manut', 'tipo_aterramento', 'cliCod', 'equipCod', 'valor')

        widgets = {
             'dataInicioOs': DateInputCustom(format='%Y-%m-%d'),
             'dataFinalOs': DateInputCustom(format='%Y-%m-%d'),
        }
