from django.contrib import admin
from . models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['categoryName', 'slug']
    prepopulated_fields = {'slug': ('categoryName',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productName', 'productPrice', 'slug', 'category', 'productStock', 'productCreatedAt', 'productUpdateAt', 'productAvailable']
    prepopulated_fields = {'slug': ('productName',)}
    list_editable = ['productPrice', 'productStock', 'productAvailable']
    list_per_page = 20
admin.site.register(Product, ProductAdmin)
