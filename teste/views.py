
from django.shortcuts import render,HttpResponse
from .models import Fornecedores



def home(request):
    fornecedores = Fornecedores.objects.all()
    return render(request, 'teste/index.html', {'fornecedores': fornecedores})

    #return render(request, 'teste/index.html')


def index(request):
    return HttpResponse('Hello World!')