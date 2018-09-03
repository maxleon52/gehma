from django.contrib import admin
from cad_clientes_app.models import tb_clientes


class tb_clientesAdmin(admin.ModelAdmin):
#AGRUPA NA PROPRIA LINHA
    #fields = (('nome', 'nomeFant'), ('cep', 'endereco', 'bairro', 'cidade', 'uf'), ('cnpj', 'cpf'), 'contato', 'email', ('tel', 'cel1', 'cel2'))

#SEPARA POR GRUPOS
    fieldsets = (
        ('DADOS PESSOAIS',{'fields': ('nome', 'nomeFant', 'cep', 'endereco', 'bairro', 'cidade', 'uf', 'cnpj', 'cpf')}),
        ('OUTROS INFORMAÇÕES',{'fields':('contato', 'email', 'tel', 'cel1', 'cel2')})
    )
# ORGANIZA A LISTA
    list_display = ('cod', 'nome', 'nomeFant', 'cep', 'endereco', 'bairro', 'cidade', 'uf', 'cnpj', 'cpf', 'dt_criacao')



admin.site.register(tb_clientes, tb_clientesAdmin)