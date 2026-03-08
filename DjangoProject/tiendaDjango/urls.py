from django.contrib import admin
from django.urls import path
from departamento import views
from producto import  views as producto
from .views import index

urlpatterns = [
    path('', index, name='welcome'),
    path('departamento/lista/', views.index, name='departamento_lista'),
    path('departamento/create/', views.create, name='departamento_create'),
    path('departamento/update/<int:pk>/', views.update, name='departamento_update'),
    path('departamento/delete/<int:pk>/', views.delete, name='departamento_delete'),
    path('producto/lista/', producto.index, name='producto_lista'),
    path('producto/create/', producto.create, name='producto_create'),
    path('producto/update/<int:pk>/', producto.update, name='producto_update'),
    path('producto/delete/<int:pk>/', producto.delete, name='producto_delete'),
]
