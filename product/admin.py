from django.contrib import admin
from .models import Product, Category, Stock
# Register your models here.

#product admin which will display the product details in the admin panel
class ProductAdmin(admin.ModelAdmin): 
    list_display = ['name', 'price', 'category',]
    search_fields = ['name', 'category__name',]
    list_filter = ['category','price',]
    list_per_page = 10

#category admin which will display the category details in the admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]
    list_filter = ['name',]
    list_per_page = 10


#stock admin which will display the stock details in the admin panel
class StockAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity',]
    search_fields = ['product__name',]
    list_filter = ['product',]
    list_per_page = 10

#registering the models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Stock, StockAdmin)
