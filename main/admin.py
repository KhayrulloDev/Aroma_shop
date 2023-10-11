from django.contrib import admin
from .models import Product, Picture, Category
from modeltranslation.admin import TranslationAdmin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Picture)
admin.site.register(Category)
