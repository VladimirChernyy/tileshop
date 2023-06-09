from django.contrib import admin

from .models import Category, Product, Rewies, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    search_help_text = 'Введите название категории'


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_help_text = 'Введите название категории'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'images',
                    'create_at', 'product_stock')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description', 'price')
    list_editable = ('product_stock',)
    list_filter = ('product_stock', 'create_at', 'price')


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rewies)
