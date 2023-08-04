from django.urls import path
from .views import EmpresaCreateview, EmpresaEditView

urlpatterns = [
    path('novo', EmpresaCreateview.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', EmpresaEditView.as_view(), name='edit_empresa'),
]
