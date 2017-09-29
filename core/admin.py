from django.contrib import admin
from core.models import Category, Subcategory, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)