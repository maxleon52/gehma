from django.forms import ModelForm
from .models import tb_equip, tb_orcamentos


class equipForm(ModelForm):
    class Meta:
        model = tb_equip
        fields = ['nome', 'modelo', 'marca', 'tensao', 'proxManu', 'numSerie', 'fotoFrente', 'fotoVerso']


class orcamentosForm(ModelForm):
    class Meta:
        model = tb_orcamentos
        fields = ['nomeEquip', 'qtd', 'valorUnit']
