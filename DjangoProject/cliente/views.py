from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Cliente
from .forms import ClienteForm

def index(request):
    clientes = Cliente.objects.all()
    paginator = Paginator(clientes, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,'cliente/lista.html',{'context':page})

def create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_lista')
    else:
        form = ClienteForm()
    return render(request,'cliente/form.html',{'form':form})

def update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request,'cliente/form.html',{'form':form})

def delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_lista')
    return render(request,'cliente/delete.html',{'cliente':cliente})