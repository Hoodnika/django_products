from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.models import Product, Category
from products.services import get_category_list_cache
from users.views import CustomLoginRequiredMixin
from version_app.models import Version
from products.forms import ProductForm, ProductModeratorForm


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_category_list_cache()

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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_list = self.get_queryset()

        for product in product_list:
            versions = Version.objects.all().filter(product=product)
            boolean_version = versions.filter(is_active=True)
            if boolean_version:
                product.version_num = boolean_version.last().version_num
                product.version_name = boolean_version.last().version_name
        context_data['object_list'] = product_list
        return context_data


# def products_to_add(request, category_pk: int):
#     context = {
#         "products_list": Product.objects.all().filter(category=category_pk),
#     }
#     return render(request, 'products/version_list.html', context)


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
#     return render(request, 'products/version_detail.html', context)


class ProductCreateView(CustomLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:category_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.object.pk})

    def get_form_class(self):
        if self.request.user == self.object.owner:
            return ProductForm
        if self.request.user.has_perms((
                'products.can_edit_published',
                'products.can_edit_description',
                'products.can_edit_category'
        )):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('products:product_list', kwargs={'category_pk': self.object.category.pk})


