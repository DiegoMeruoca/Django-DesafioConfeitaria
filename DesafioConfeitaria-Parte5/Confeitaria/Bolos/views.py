from django.shortcuts import render, redirect
from .models import Bolo
from .form import BoloForm

def home(request):
    return render(request,"Bolos/home.html")

def listagembolo(request):
    data = {}
    data["bolos"]= Bolo.objects.all()
    return render(request,"Bolos/listagembolo.html", data)

def cadastrobolo(request):  # Cria a função de cadastro
    data = {}  # Cria um dicionário vazio
    form = BoloForm(request.POST or None)  # Cria um form
    # recebendo os dados do POST do bt Salvar ou vazio
    if form.is_valid():  # Testa se o form é valido
        form.save()  # Salva os dados no Banco de Dados
        return redirect('url_listagembolo')  # Redireciona
    data['form'] = form  # Adiciona o form criado no dicionario
    return render(request, "Bolos/cadastro.html", data)