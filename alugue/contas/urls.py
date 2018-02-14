from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, dashboard

#URLS PARA APP CONTAS
urlpatterns = [
    path('', dashboard),
    path('entrar/', auth_views.login,{'template_name':'contas/loggin.html'}, name='entrar'),
    path('sair/', auth_views.logout,{'next_page':'/'}, name='logout'),
    path('cadastre-se/', register),



]