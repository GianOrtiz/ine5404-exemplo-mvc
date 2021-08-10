from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Produto

class StockView(LoginRequiredMixin, generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        """Retorna todos os produtos no banco de dados"""
        return Produto.objects.all()

class ProductCreateView(generic.CreateView):
    model = Produto
    fields = ['codigo', 'nome', 'valor', 'quantidade']

class ProdutDetailView(generic.DetailView):
    model = Produto

class ProductDeleteView(generic.DeleteView):
    model = Produto
    success_url = reverse_lazy('index')

class ProductUpdateView(generic.UpdateView):
    model = Produto
    fields = ['codigo', 'nome', 'valor', 'quantidade']

# CreateProductView

# EditProductView
