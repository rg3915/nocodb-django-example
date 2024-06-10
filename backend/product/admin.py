from django.contrib import admin

from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)
    list_filter = ('category',)


admin.site.register(Category)
