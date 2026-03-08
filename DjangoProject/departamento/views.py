from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Departamento
from .forms import DepartamentoForm

def index(request):
    departamentos = Departamento.objects.all()
    paginator = Paginator(departamentos, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'departamento/lista.html', {'context': page})

def create(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departamento_lista')
    else:
        form = DepartamentoForm()
    return render(request, 'departamento/form.html', {'form': form})

def update(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('departamento_lista')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'departamento/form.html', {'form': form})

def delete(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        departamento.delete()
        return redirect('departamento_lista')
    return render(request, 'departamento/delete.html', {'departamento': departamento})
