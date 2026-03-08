from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Producto
from .forms import ProductoForm


def index(request):
    productos = Producto.objects.all()

    paginator = Paginator(productos, 5)

    page_number = request.GET.get('page')

    page = paginator.get_page(page_number)

    return render(request, 'producto/lista.html', {'context': page})


def create(request):
    if request.method == 'POST':

        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('producto_lista')

    else:
        form = ProductoForm()

    return render(request, 'producto/form.html', {'form': form})


def update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':

        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid():
            form.save()
            return redirect('producto_lista')

    else:
        form = ProductoForm(instance=producto)

    return render(request, 'producto/form.html', {'form': form})


def delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('producto_lista')

    return render(request, 'producto/delete.html', {'producto': producto})
