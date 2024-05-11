from django.urls import path

from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<str:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<str:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
