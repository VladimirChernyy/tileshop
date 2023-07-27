from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    template = 'order/create.html'
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, template, {'order': order})
    form = OrderCreateForm()
    return render(request, template, {'cart': cart, 'form': form})
