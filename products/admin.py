from django.contrib import admin

from products.models import Category, Product


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'view_count',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)