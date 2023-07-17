from django.contrib import admin

from .models import Category, Product, Reviews, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    search_help_text = 'Введите название категории'


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_help_text = 'Введите название категории'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'images',
                    'create_at', 'available')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description', 'price')
    list_editable = ('available',)
    list_filter = ('available', 'create_at', 'price')


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Reviews)
