from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente
# Create your views here.

def cadastrar_cliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_cliente')
    
    clientes = Cliente.objects.all()
    return render(request, 'cadastrar_cliente.html', {'form': form, 'clientes': clientes})