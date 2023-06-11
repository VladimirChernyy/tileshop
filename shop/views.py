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


def category_products(request, slug):
    print(request.content_params)
    category = Category.objects.filter(slug=slug)
    products = category.products.all()
    template = 'shop/category.html'
    context = {
        'products': products,
        'category': category
    }
    return render(request, template, context)


def rewies(request):
    template = 'shop/rewies.html'
    return render(request, template)
