from django.shortcuts import render


def index(request):
    template = 'shop/index.html'
    context = {
        'title': 'Магазин',
        'body': 'Магазин инструмента',
    }
    return render(request, template, context)


def category(request):
    template = 'shop/category.html'
    return render(request, template)


def rewies(request):
    template = 'shop/rewies.html'
    return render(request, template)
