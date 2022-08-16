from django.contrib import admin
from product.models import Product, Category
from django.utils.html import format_html


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'created_at']
    search_fields = ['name', 'status', 'created_at']
    list_filter = ['status']
    ordering = ('id','name', 'status', 'created_at')
    prepopulated_fields = {'name': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img height="100" src="{}" />'.format(obj.image.url))
    image_tag.short_description = 'Product Image'

    list_display = ['id', 'image_tag', 'name', 'category', 'price', 'quantity', 'sku', 'status', 'created_at']
    search_fields = ['long_desc', 'category__name', 'slug', 'name', 'price', 'quantity', 'sku', 'status']
    list_filter = ['status', 'category', 'price', 'created_at']
    ordering = ('id', 'name', 'category', 'price', 'quantity', 'sku', 'status', 'created_at')
    readonly_fields = ('image_tag',)

admin.site.register(Product, ProductAdmin)
