from django.forms import ModelForm, DateInput
from .models import tb_equip, tb_orcamentos


class DateInputCustom(DateInput):
       input_type = 'date'

class equipForm(ModelForm):
    class Meta:
        model = tb_equip
        fields = ['nome', 'modelo', 'marca', 'tensao', 'proxManu', 'numSerie', 'fotoFrente', 'fotoVerso', 'cliCod']
        widgets = {
            'proxManu': DateInputCustom(format='%Y-%m-%d'),
        }


class orcamentosForm(ModelForm):
    class Meta:
        model = tb_orcamentos
        fields = ['nomeEquip', 'qtd', 'valorUnit']