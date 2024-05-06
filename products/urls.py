from django.urls import path

from products.apps import ProductsConfig
from products.views import CategoryListView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = ProductsConfig.name

urlpatterns = [
    path('home/', CategoryListView.as_view(), name='category_list'),
    path('product_list/<int:category_pk>/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
