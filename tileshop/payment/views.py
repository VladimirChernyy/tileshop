from http import HTTPStatus

from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings
import stripe

from shop.models import Product
from cart.cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'payment/success.html'


class CancelView(TemplateView):
    template_name = 'payment/cancel.html'


class CreateCheckoutSession(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        *product_ids, = cart.cart
        products = Product.objects.filter(id__in=product_ids)
        line_items = []
        for product in products:
            line_items.append({
                'price': product.stripe_id,
                'quantity': cart.cart[str(product.id)]['quantity'],
            })
        domain = 'http://localhost:8000/payment'
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                mode='payment',
                success_url=domain + '/success/',
                cancel_url=domain + '/cancel/',
            )
        except Exception as e:
            return str(e)
        return redirect(checkout_session.url, code=HTTPStatus.SEE_OTHER)
