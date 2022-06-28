from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):    
    list_display = ('name', 'price', 'creator')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Product,ProductAdmin)