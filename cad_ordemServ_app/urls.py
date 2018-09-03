from django.urls import path
from .views import lista_clientes_os, lista_Equip_os, SelecClientes_os, SelecEquip_os, listaOrdemServico, novaOS

urlpatterns = [
    path('lista_clientes_os/', lista_clientes_os, name='lista_clientes_os'),  # caminho(APP) e função na view
    path('lista_Equip_os/', lista_Equip_os, name='lista_Equip_os'),  # caminho(APP) e função na view
    path('listaOrdemServico/', listaOrdemServico, name='listaOrdemServico_urls'),  # caminho(APP) e função na view

    path('SelecClientes_os/<int:id>', SelecClientes_os, name='SelecClientes_os'),  # caminho(APP) e função na view
    path('SelecEquip_os/<int:id>', SelecEquip_os, name='SelecEquip_os'),  # caminho(APP) e função na view

    path('novaOS/', novaOS, name='novaOS_urls'),  # caminho(APP) e função na view
]
