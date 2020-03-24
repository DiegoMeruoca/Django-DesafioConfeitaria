from django.db import models

class Bolo(models.Model):  # Cria a classe de model Transação
    nome = models.CharField(max_length=100)
    # Cria o field nome com o tipo char e tamanho maximo 100
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    # Tipo decimal, com 7 digitos no total e 2 depois da virgula.
    detalhes = models.TextField(null=True, blank=True)
    # Tipo text, Pode ser nulo ou vazio...

    def __str__(self):  # Permite exibir uma string como identificação
        return self.nome  # Exibe o nome como identificação
