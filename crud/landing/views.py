from django.shortcuts import render, redirect
from .models import Aluno, Usuario

# Create your views here.

def index(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()
        
        data_aluno = Aluno()
        data_aluno.nome = request.POST['nome']
        data_aluno.frase = request.POST['frase']
        data_aluno.save()
        
    return render(request, 'index.html')

def listar(request):
    listar_frase = Aluno.objects.filter(ativo=True).all()
    args = {
        'listar_frase': listar_frase
    }

    return render(request, 'lista.html', args)


def deletar(request, id):
    item = Aluno.objects.get(id=id)

    if item is not None:
        item.ativo = False
        item.save()
        return redirect('/alunos/lista')

    return render(request, 'lista.html')

def home(request):
    return render(request, 'home.html')


def login(request): 
    if request.method == 'POST':
        usuario = Usuario.objects.filter(email=request.POST['email'], senha=request.POST['senha'])
        # if usuario is not None:
            # return redirect('/')
        
        return redirect('/alunos/cadastro')

    # usuario n existe
    return render(request, 'login.html')
    