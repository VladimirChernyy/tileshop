from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def index(request):
    categories = Category.objects.select_related()
    template = 'shop/index.html'
    context = {
        'title': 'Магазин',
        'body': 'Магазин инструмента',
        'categories': categories
    }
    return render(request, template, context)


def category_products(request, category):
    print(request)
    category = Category.objects.filter(slug=category)
    products = category.products.select_related()
    template = 'shop/category.html'
    context = {
        'products': products,
        'category': category
    }
    return render(request, template, context)


def rewies(request):
    template = 'shop/rewies.html'
    return render(request, template)
