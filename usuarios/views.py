from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def cadastro(request):
    return render(request, 'cadastro.html')

def login (request):
    return render(request,'login.html')

def valida_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Aqui você pode adicionar lógica para salvar os dados do usuário no banco de dados
        
        return HttpResponse(f'Cadastro realizado com sucesso! Nome: {nome}, Email: {email}')
   