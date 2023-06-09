from django.contrib import admin

from .models import Category, Product, Rewies


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    search_help_text = 'Введите название категории'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'images',
                    'create_at', 'product_stock')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    list_editable = ('product_stock',)
    list_filter = ('product_stock', 'create_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rewies)
