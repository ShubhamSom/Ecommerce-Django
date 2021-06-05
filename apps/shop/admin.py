from django.contrib import admin

# Register your models here.
from .models import Category, Product

# admin.site.register(Category)
# admin.site.register(Product)
#  https://youtu.be/zPPfSEqUDTs


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
