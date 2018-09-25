from django.urls import path
from .views import lista_clientes, atualizaCliente, novoCliente, deleteCliente, pdf_generation

urlpatterns = [
    path('listaClientes/', lista_clientes, name='lista_clientes'), #caminho(APP) e função na view
    path('novoClientes/', novoCliente, name='novoCliente'), #caminho(APP) e função na view
    path('atualizaClientes/<int:id>', atualizaCliente, name='atualizaCliente'), #caminho(APP) e função na view
    path('deleteClientes/<int:id>', deleteCliente, name='deleteCliente'), #caminho(APP) e função na view
    path('pdf_generation/', pdf_generation, name='pdf_generation_urls'), #caminho(APP) e função na view
]
