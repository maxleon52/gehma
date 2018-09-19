from django.urls import path
from .views import listaEquip, atualizaEquip, deleteEquip, historicoOs

urlpatterns = [
    path('listaEquip/', listaEquip, name='listaEquip'),  # caminho(APP) e função na view
    path('atualizaEquip/<int:id>', atualizaEquip, name='atualizaEquip'), #caminho(APP) e função na view
    path('deleteEquip/<int:id>', deleteEquip, name='deleteEquip'), #caminho(APP) e função na view

    path('historicoOs/<int:id>', historicoOs, name="historico_urls")
]
