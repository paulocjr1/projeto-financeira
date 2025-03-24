from django.urls import path
from .views import cadastrar_cliente



urlpatterns = [
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente')
]
