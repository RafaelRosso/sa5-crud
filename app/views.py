from django.shortcuts import render, redirect
from app.models import Pessoa
# Create your views here.
def index(request):
    dados = Pessoa.objects.all()
    inverso = dados[::-1]
    dados = inverso[:10]
    return render(request, "app/index.html", context={"dados":dados})

def criar(request):
    nome = ""
    email = ""
    nascimento = ""
    pais = ""
    if request.POST:
        nome = request.POST.get("nome")
        nascimento = request.POST.get("nascimento")
        email = request.POST.get("email")
        pais = request.POST.get("pais") 
        Pessoa.objects.create(nome=nome,nascimento=nascimento,email=email,pais=pais)
    return render(request, "app/criar.html", context={"nome":nome})

def pesquisar(request):
    dados = {}
    if request.GET:
        nome_busca = request.GET.get("nome")
        dados['dados'] =Pessoa.objects.filter(nome__icontains=nome_busca)
    else:
        dados['dados'] = Pessoa.objects.all()
    return render(request, "app/pesquisar.html", dados)

def atualizar(request,id=0):
    dados = {}
    if id:
        if request.POST:
            # Como estou usando validação de preenchimento, não estou passando o segundo parametro no get
            dados = Pessoa.objects.get(id=id)
            dados.nome = request.POST.get("nome")
            dados.nascimento = request.POST.get("nascimento")
            dados.email = request.POST.get("email")
            dados.pais = request.POST.get("pais")
            dados.save()
            return redirect (atualizar)
    
        dados["dados"] = Pessoa.objects.get(id=id)
        return render(request, "app/atualizar.html", context=dados)
    nome_busca = request.GET.get("nome")
    if nome_busca:
        dados['dados'] =Pessoa.objects.filter(nome__icontains=nome_busca)
    else:
        dados['dados'] = Pessoa.objects.all()    
    return render(request, "app/exibe_atualizar.html", context=dados)

def deletar(request,id=0):
    dados = {}
    if id:
        dados = Pessoa.objects.get(id=id)
        dados.delete()
        return redirect(deletar)
    nome_busca = request.GET.get("nome")
    if nome_busca:
        dados['dados'] =Pessoa.objects.filter(nome__icontains=nome_busca)
    else:
        dados['dados'] = Pessoa.objects.all()     
    return render(request, "app/exibe_deletar.html", context=dados)
    


