from django.urls import path
from .views import DocumentoCreateview

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreateview.as_view(), name='create_documentos'),
    # path('editar/<int:pk>/', EmpresaEditView.as_view(), name='edit_empresa'),
]
