from django.shortcuts import render
from loja_online.models import Categoria, Produto

# Create your views here.

def index(request):
    num_produtos = Produto.objects.all().count()
    num_camisas = Produto.objects.filter(categoria="1").count()

    context = {
        'num_produtos': num_produtos,
        'num_camisas': num_camisas,
    }



    return render(request, 'index.html', context=context)


def listar_produtos(request):
    produtos = Produto.objects.filter(product_status="publicado")
    produtos_publicados = produtos.count()
    context = {
        "produtos":produtos,
        "produto_publicados":produtos_publicados
    }

    return render(request, 'produtos.html')
