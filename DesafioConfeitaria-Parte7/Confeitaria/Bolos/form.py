from django.forms import ModelForm
from .models import Bolo

class BoloForm(ModelForm):
    class Meta:
        model = Bolo
        fields = ["nome","preco","detalhes"]