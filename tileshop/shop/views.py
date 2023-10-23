from django.shortcuts import render, get_object_or_404, redirect

from cart.forms import CartAddProductForm
from shop.forms import ReviewCreateForm
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


def product_detail(request, product_slug):
    product = get_object_or_404(Product,
                                slug=product_slug,
                                available=True)

    cart_product_form = CartAddProductForm()
    create_review_form = ReviewCreateForm()
    templates = 'shop/product_detail.html'
    context = {
        'title': product.name,
        'product': product,
        'cart_product_form': cart_product_form,
        'create_review_form': create_review_form,
    }
    return render(request, templates, context)


def create_review(request, product_id):
    template = 'shop/product_detail.html'
    product = get_object_or_404(Product, id=product_id)
    create_review_form = ReviewCreateForm(request.POST or None)
    if create_review_form.is_valid():
        review = create_review_form.save(commit=False)
        review.author = request.user
        review.product = product
        review.save()
        return redirect('shop:product', product.slug)
    context = {
        'product': product,
    }
    return render(request, template, context)
