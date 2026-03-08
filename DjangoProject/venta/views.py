from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Venta
from .forms import VentaForm

def index(request):
    ventas = Venta.objects.all()
    paginator = Paginator(ventas,5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,'venta/lista.html',{'context':page})

def create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_lista')
    else:
        form = VentaForm()
    return render(request,'venta/form.html',{'form':form})

def update(request,pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta_lista')
    else:
        form = VentaForm(instance=venta)
    return render(request,'venta/form.html',{'form':form})

def delete(request,pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('venta_lista')
    return render(request,'venta/delete.html',{'venta':venta})