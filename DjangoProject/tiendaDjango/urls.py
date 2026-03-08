from django.contrib import admin
from django.urls import path
from departamento import views as departamento
from producto import views as producto
from cliente import views as cliente
from venta import views as venta
from .views import index

urlpatterns = [

path('', index, name='welcome'),

path('departamento/lista/', departamento.index, name='departamento_lista'),
path('departamento/create/', departamento.create, name='departamento_create'),
path('departamento/update/<int:pk>/', departamento.update, name='departamento_update'),
path('departamento/delete/<int:pk>/', departamento.delete, name='departamento_delete'),

path('producto/lista/', producto.index, name='producto_lista'),
path('producto/create/', producto.create, name='producto_create'),
path('producto/update/<int:pk>/', producto.update, name='producto_update'),
path('producto/delete/<int:pk>/', producto.delete, name='producto_delete'),
path('producto/precio/<int:pk>/', producto.obtener_precio, name='producto_precio'),

path('cliente/lista/', cliente.index, name='cliente_lista'),
path('cliente/create/', cliente.create, name='cliente_create'),
path('cliente/update/<int:pk>/', cliente.update, name='cliente_update'),
path('cliente/delete/<int:pk>/', cliente.delete, name='cliente_delete'),

path('venta/lista/', venta.index, name='venta_lista'),
path('venta/create/', venta.create, name='venta_create'),
path('venta/update/<int:pk>/', venta.update, name='venta_update'),
path('venta/delete/<int:pk>/', venta.delete, name='venta_delete'),

]