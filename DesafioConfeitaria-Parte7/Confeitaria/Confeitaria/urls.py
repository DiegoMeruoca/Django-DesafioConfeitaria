"""Confeitaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Bolos.views import home, listagembolo, cadastrobolo, atualizar_bolo, deletar_bolo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('', listagembolo, name="url_listagembolo"),
    path('cadastro/', cadastrobolo, name="url_cadastro"),
    path('atualizar/<int:pk>', atualizar_bolo, name="url_atualizar"),  # Cria a
    # rota atualizar, nesse caso adicionando um paramentro PK do tipo inteiro
    path('deletar/<int:pk>', deletar_bolo, name="url_deletar"),  # Cria a
    # rota deletar, nesse caso adicionando um paramentro PK do tipo inteiro
]