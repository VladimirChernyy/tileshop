from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from shop.models import Category, Product


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
    cart_product_form = CartAddProductForm()
    if not subcategory:
        products = category.products.select_related()
        template = 'shop/category_list.html'
        context = {
            'title': category.slug,
            'products': products,
            'cart_product_form': cart_product_form,
        }
        return render(request, template, context)
    subcategory = category.subcategory.select_related()
    template = 'shop/index.html'
    context = {
        'title': 'Магазин',
        'categories': subcategory,
    }
    return render(request, template, context)


def product_detail(request, pk, product_slug):
    product = get_object_or_404(Product,
                                id=pk,
                                slug=product_slug,
                                available=True)

    cart_product_form = CartAddProductForm()
    templates = 'cart/create.html'
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, templates, context)


def reviews(request):
    template = 'shop/reviews.html'
    return render(request, template)
