from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.models import Product, Category, Blog


class CategoryListView(ListView):
    model = Category

# def home(request):
#     context = {
#
#         "category_list": Category.objects.all(),
#     }
#     return render(request, 'products/category_list.html', context)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.all().filter(category=self.kwargs['category_pk'])


# def products_to_add(request, category_pk: int):
#     context = {
#         "products_list": Product.objects.all().filter(category=category_pk),
#     }
#     return render(request, 'products/blog_list.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


# def product_detail(request, pk: int):
#     context = {
#         # "object": get_object_or_404(Product, pk=pk),
#         'object': Product.objects.get(pk=pk),
#     }
#     return render(request, 'products/blog_detail.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'category', 'image', )
    success_url = reverse_lazy('products:category_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'price', 'category', 'image',)
    success_url = reverse_lazy('products:category_list')

    def get_success_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('products:product_list', kwargs={'category_pk': self.object.category.pk})


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.all().filter(published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'published')
    success_url = reverse_lazy('products:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'published', 'published')
    success_url = reverse_lazy('products:blog_list')

    def get_success_url(self):
        return reverse('products:blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('products:blog_list')

