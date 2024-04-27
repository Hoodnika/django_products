from django.urls import path

from products.apps import ProductsConfig
from products.views import home, products_to_add, product_detail

app_name = ProductsConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('products_to_add/', products_to_add, name='products_to_add'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail')
]
