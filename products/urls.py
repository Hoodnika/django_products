from django.urls import path

from products.apps import ProductsConfig
from products.views import *

app_name = ProductsConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('product_list/<int:category_pk>/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # path('blog/', BlogListView.as_view(), name='blog_list'),
    # path('blog_detail/<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    # path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    # path('blog/<str:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    # path('blog/<str:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
