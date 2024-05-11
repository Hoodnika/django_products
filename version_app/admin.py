from django.contrib import admin

from version_app.models import Version


@admin.register(Version)
class AdminVersion(admin.ModelAdmin):
    list_display = ('version_num', 'version_name', 'product', 'is_active', 'created_at', 'updated_at',)
    list_filter = ('version_num', 'product', 'is_active', 'updated_at',)
    search_fields = ('version_name', 'product', 'version_num',)
