from django.urls import path
from .views import novoEquip, orcamentos, novoOrcamento

urlpatterns = [
    path('novoEquip/', novoEquip, name='novoEquip_urls'), #caminho(APP) e função na view
    path('orcamentos/', orcamentos, name='orcamentos_urls'), #caminho(APP) e função na view
    path('novoOrcamento/', novoOrcamento, name='novoOrcamento_urls'), #caminho(APP) e função na view
]
