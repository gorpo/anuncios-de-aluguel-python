from django.urls import path
from .views import home,cadastroImoveis, post
urlpatterns = [
    #VASIO ENCAMINHA PARA LISTAGEM DE IMOVEIS
    path('', home),
    path('cadastroimoveis/', cadastroImoveis),
    path('buscar/', post),



]
