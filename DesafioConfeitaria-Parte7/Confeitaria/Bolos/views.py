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

def atualizar_bolo(request, pk):  # Cria a função de update,
    # que recebe a pk, para saber qual registro atualizar
    data = {}  # Cria um dicionário vazio
    bolo = Bolo.objects.get(pk=pk)  # Cria a variave transacao que
    # recebe do banco a transação referente a PK que a view recebeu
    form = BoloForm(request.POST or None, instance=bolo)  # Cria
    # um form recebendo os dados da transacao referente à PK
    if form.is_valid():  # Testa se o form é valido
        form.save()  # Salva os dados no Banco de Dados
        return redirect('url_listagembolo')  # Redireciona
    data['form'] = form  # Adiciona o form criado no dicionario
    return render(request, "Bolos/cadastro.html", data)

def deletar_bolo(request, pk):  # Cria a função de delete,
    # que recebe a pk, para saber qual registro deletar
    bolo = Bolo.objects.get(pk=pk)  # Cria a variave transacao que
    # recebe do banco a transação referente a PK que a view recebeu
    bolo.delete()  # Deleta a transação
    return redirect('url_listagembolo')  # Redireciona para listagem

