
from django.urls import path
from django.views.decorators.cache import cache_page

from products.apps import ProductsConfig
from products.views import CategoryListView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = ProductsConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('product_list/<int:category_pk>/', ProductListView.as_view(), name='product_list'),
    # path('product_list/<int:category_pk>/', cache_page(100)(ProductListView.as_view()), name='product_list'),
    path('product_detail/<int:pk>/', cache_page(20)(ProductDetailView.as_view()), name='product_detail'),
    path('products/create/', cache_page(20)(ProductCreateView.as_view()), name='product_create'),
    path('product/<int:pk>/update/', cache_page(60)(ProductUpdateView.as_view()), name='product_update'),
    path('product/<int:pk>/delete/', cache_page(10)(ProductDeleteView.as_view()), name='product_delete'),

    # path('blog/', BlogListView.as_view(), name='blog_list'),
    # path('blog_detail/<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    # path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    # path('blog/<str:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    # path('blog/<str:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
