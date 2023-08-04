
from django.urls import path
from .views import  FuncionariosListView, FuncionarioEditView, FuncionarioDeleteView, FuncionarioCreateView
from .models import Funcionario

urlpatterns = [
    path('list', FuncionariosListView.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioEditView.as_view(), name='edit_funcionario'),
    path('delete/<int:pk>/', FuncionarioDeleteView.as_view(), name='delete_funcionario'),
    path('novo/', FuncionarioCreateView.as_view(), name='create_funcionario'),
 
]
