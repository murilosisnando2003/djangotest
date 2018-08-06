from django.forms import ModelForm
from .models import Fornecedores

class FornecedoresForm(ModelForm):
    class Meta:
        model = Fornecedores
        fields = ['name','email','status','contato']
