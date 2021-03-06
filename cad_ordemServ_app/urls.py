from django.urls import path
from .views import lista_clientes_os, lista_Equip_os, deleteOs, finalizaOs, SelecClientes_os, SelecEquip_os, listaOrdemServico, novaOS, CreateOs, atualizaOs, pdf_rel_assisTec

urlpatterns = [
    path('lista_clientes_os/', lista_clientes_os, name='lista_clientes_os'),  # caminho(APP) e função na view
    path('lista_Equip_os/', lista_Equip_os, name='lista_Equip_os'),  # caminho(APP) e função na view
    path('listaOrdemServico/', listaOrdemServico, name='listaOrdemServico_urls'),  # caminho(APP) e função na view
    path('atualizaOs/<int:id>', atualizaOs, name='atualizaOs_urls'),  # caminho(APP) e função na view
    path('deleteOs/<int:id>', deleteOs, name='deleteOs_urls'), #caminho(APP) e função na view
    path('finalizaOs/<int:id>', finalizaOs, name='finalizaOs_urls'), #caminho(APP) e função na view


    path('SelecClientes_os/<int:id>', SelecClientes_os, name='SelecClientes_os'),  # caminho(APP) e função na view
    path('SelecEquip_os/<int:id>', SelecEquip_os, name='SelecEquip_os'),  # caminho(APP) e função na view

    path('novaOS/', novaOS, name='novaOS_urls'),  # caminho(APP) e função na view
    path('create/os/leonardo/', CreateOs.as_view(), name="create_os_leo"),

    path('pdf_rel_assisTec/<int:id>', pdf_rel_assisTec, name='pdf_rel_assisTec_urls'), #caminho(APP) e função na view


]
