from django.shortcuts import render, redirect
from app.models import Pessoa
# Create your views here.
def index(request):
    nome = ""
    email = ""
    nascimento = ""
    pais = ""
    dados = Pessoa.objects.all()

    if request.POST:
        nome = request.POST.get("nome")
        nascimento = request.POST.get("nascimento")
        email = request.POST.get("email")
        pais = request.POST.get("pais") 
        Pessoa.objects.create(nome=nome,nascimento=nascimento,email=email,pais=pais)
    inverso = dados[::-1]
    dados = inverso[:10]
    return render(request, "app/index.html", context={"dados":dados})

def atualizar(request,id):
    dados = Pessoa.objects.get(id=id)
    if request.POST:
        dados.nome = request.POST.get("nome")
        dados.nascimento = request.POST.get("nascimento")
        dados.email = request.POST.get("email")
        dados.pais = request.POST.get("pais")
        dados.save()
        return redirect (index)
    return render(request, "app/atualizar.html", context={"dados":dados})

def deletar(request,id=0):
    dados = Pessoa.objects.get(id=id)
    dados.delete()
    return redirect(index)
    


