from django.shortcuts import render, get_object_or_404

from .models import Category, Product, SubCategory


def index(request):
    categories = Category.objects.select_related()
    template = 'shop/index.html'
    context = {
        'title': 'Магазин',
        'categories': categories
    }
    return render(request, template, context)


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = category.subcategory.select_related()
    if not subcategory:
        products = category.products.select_related()
        template = 'shop/category_list.html'
        context = {
            'title': category.slug,
            'products': products,
        }
        return render(request, template, context)
    subcategory = category.subcategory.select_related()
    template = 'shop/index.html'
    context = {
        'title': 'Магазин',
        'categories': subcategory,
    }
    return render(request, template, context)


def product_list(request, product_slug):
    pass


def reviews(request):
    template = 'shop/reviews.html'
    return render(request, template)
