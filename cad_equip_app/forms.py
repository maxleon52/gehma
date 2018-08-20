from django.forms import ModelForm
from .models import tb_equip


class equipForm(ModelForm):
    class Meta:
        model = tb_equip
        fields = ['nome', 'modelo', 'marca', 'tensao', 'proxManu', 'numSerie', 'fotoFrente', 'fotoVerso']
