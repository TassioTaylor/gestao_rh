from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from apps.empresa.models import Empresa
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse



class EmpresaCreateview(CreateView):
    model = Empresa
    fields = ["nome"]
 

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()

        return HttpResponse('ok')
    

class EmpresaEditView(UpdateView):
    model = Empresa
    fields = ["nome"]