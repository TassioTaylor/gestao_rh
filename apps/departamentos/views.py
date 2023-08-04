from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento
from django.urls import reverse_lazy


class DepartamentosListView(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentosCreateView(CreateView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamentos')

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentosCreateView, self).form_valid(form)
    

class DepartamentosUpdateView(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentosDeleteView(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
    