
from django.urls import path
from .views import DepartamentosListView, DepartamentosCreateView, DepartamentosUpdateView, DepartamentosDeleteView

urlpatterns = [
    path('list', DepartamentosListView.as_view(), name='list_departamentos'),
    path('novo', DepartamentosCreateView.as_view(), name='create_departamento'),
    path('editar/<int:pk>/', DepartamentosUpdateView.as_view(), name='update_departamento'),
    path('delete/<int:pk>/', DepartamentosDeleteView.as_view(), name='delete_departamento'),

]
