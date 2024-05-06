from django.contrib import admin

from products.models import Category, Product, Blog


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'view_count',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('pk', 'title', 'view_count',)
    list_filter = ('published',)
    search_fields = ('title', 'content',)
