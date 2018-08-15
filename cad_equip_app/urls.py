from django.urls import path
from .views import lista_equipamentos

urlpatterns = [
    path('listaEquip/', lista_equipamentos), #caminho(APP) e função na view
]
