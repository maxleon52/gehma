from django.contrib import admin
from .models import tb_os, tb_historico


class tb_osAdmin(admin.ModelAdmin):
    # fieldsets = (
    #   ('OUTROS', {'fields': ('cod', 'defReclamado', 'defConstatado')}), #ESTA LINHA ESTA DANDO ERRO DE KEY, VER COM LEONARDO O MOTIVO DO ERRO
    #  ('DADOS PRINCIPAIS', {'fields': ( 'ServRealizado', 'dataInicioOs', 'dataFinalOs')}),
    # ('CLIENTE E EQUIPAMENTO', {'fields': ('cliCod', 'equipCod')}),
    # ('INTERVENÇÃO', {'fields': ('tipo_serv', 'tipo_manut', 'tipo_aterramento')})
    # )
    # ORGANIZA A LISTA
    list_display = ('cod', 'defReclamado', 'dataOs', 'dataInicioOs', 'dataFinalOs', 'cliCod', 'equipCod')


class tb_historicoAdmin(admin.ModelAdmin):
    list_display = ('data', 'histReclamado', 'hConstatado', 'hServRealizado', 'hOsCod')


admin.site.register(tb_os, tb_osAdmin)
admin.site.register(tb_historico, tb_historicoAdmin)

