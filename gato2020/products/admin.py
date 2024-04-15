from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'package_weight', 'arabica', 'robusta', 'image', 'origin', 'description')

    list_filter = ('category', 'name', 'package_weight', 'arabica', 'robusta')

    search_fields = ['name', 'package_weight', 'arabica', 'robusta', 'origin', 'description']

    ordering = ('category', 'name', 'package_weight', 'arabica', 'robusta', 'origin')

    fieldsets = (
        ('Продукти', {
            'fields': ('category', 'name', 'package_weight', 'arabica', 'robusta', 'image', 'origin', 'description')
        }),
    )
