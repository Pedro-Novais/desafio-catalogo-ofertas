from django.urls import path
from ..api import ProductApi
from ..views.view import index

urlpatterns = [
    path('api/products/', ProductApi.as_view(), name='get_products'),
    path('', index, name='index')
    ]