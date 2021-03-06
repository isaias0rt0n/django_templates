from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    nome_empresa = "OrtonSec"
    descricao_empresa = "Conteúdos a nível engenharia"

    contato_empresa = {
        "endereco": "Rua Cel. Rangel",
        "telefone": "99999-9999",
        "email": "isaiasorton@gmail.com"
    }

    # redenriza a page index.html passando variáveis como parâmetro para serem usadas na page
    return render(request, 'index.html', {'nome_empresa': nome_empresa, 'descricao_empresa': descricao_empresa, 'contato_empresa': contato_empresa})


def contact(request, id=5):
    return HttpResponse("pagina contatos", id)


def about(request):
    return HttpResponse("Pagina sobre")
