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

    cursos_home = {
        "1": {"titulo": "Django Fundamentos", "descricao": "Aprenda toda a base do Django!!"},
        "2": {"titulo": "Flask Fundamentos", "descricao": "Aprenda toda a base do Flask!!"},
        "3": {"titulo": "Python Orientação a Objetos", "descricao": "Entenda como funciona à orientação a objetos"},
    }

    # redenriza a page index.html passando variáveis como parâmetro para serem usadas na page
    return render(request, 'empresa/index.html', {'nome_empresa': nome_empresa, 'descricao_empresa': descricao_empresa, 'contato_empresa': contato_empresa,
                                          'cursos_home': cursos_home})


def contact(request):
    return render(request, 'empresa/contact.html')


def about(request):
    return render(request, 'empresa/about.html')
