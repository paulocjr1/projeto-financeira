from django.shortcuts import render, redirect
from .forms import ClienteForm
# Create your views here.

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'cadastrar_cliente.html', {'form': form})