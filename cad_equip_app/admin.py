from django.contrib import admin
from cad_equip_app.models import tb_equip


class tb_equipAdmin(admin.ModelAdmin):
# AGRUPA NA PROPRIA LINHA
    # fields = ('nome', 'modelo', 'marca', 'tensao', 'proxManu', 'numSerie','fotoFrente', 'fotoVerso'))

# SEPARA POR GRUPOS
    fieldsets = (
        ('DADOS PRINCIPAIS', {'fields': ('nome', 'modelo', 'marca', 'tensao', 'proxManu', 'numSerie')}),
        ('OUTRAS INFORMAÇÕES',{'fields':('fotoFrente', 'fotoVerso')})
    )
#ORGANIZA A LISTA
    list_display = ('cod', 'nome', 'modelo', 'marca', 'tensao', 'proxManu', 'numSerie', 'fotoFrente', 'fotoVerso')




admin.site.register(tb_equip, tb_equipAdmin)