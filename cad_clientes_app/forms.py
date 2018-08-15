from django.forms import ModelForm
from .models import tb_clientes

class clienteForm(ModelForm):
    class Meta:
        model = tb_clientes
        fields = ['nome','nomeFant','cep','endereco','bairro','cidade','uf','cnpj','cpf','contato','email','tel','cel1','cel2']