
from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Fornecedores
from .forms import FornecedoresForm



def home(request):
    fornecedores = Fornecedores.objects.all()
    return render(request, 'app/fornecedores.html', {'fornecedores': fornecedores})
 

    #return render(request, 'teste/index.html')

def fornecedor_delete(request, id):
    fornecedor = get_object_or_404(Fornecedores, pk=id)

    if request.method == 'POST':
        fornecedor.delete()
        return redirect('app')

    return render(request, 'app/fornecedor_delete_confirm.html', {'fornecedor': fornecedor})    
