from django.shortcuts import render, get_object_or_404

from products.models import Product, Category


def home(request):
    context = {
        "products_list": Product.objects.all(),
        "category_list": Category.objects.all(),
    }
    return render(request, 'products/home.html', context)


def products_to_add(request):
    context = {
        "products_list": Product.objects.all(),
    }
    return render(request, 'products/products_to_add.html', context)


def product_detail(request, pk):
    context = {
        "object": get_object_or_404(Product, pk=pk),
    }
    return render(request, 'products/product_detail.html', context)
