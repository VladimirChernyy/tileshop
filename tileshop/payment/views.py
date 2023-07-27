from http import HTTPStatus

from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings
import stripe


from orders.models import OrderItem
from shop.models import Product
from cart.cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'payment/success.html'


class CancelView(TemplateView):
    template_name = 'payment/cancel.html'


# class CheckTemplate(TemplateView):
#     template_name = 'payment/checkpayment.html'
#
#     def get_context_data(self, **kwargs):
#         product_id = self.kwargs['product_id']
#         product = get_object_or_404(OrderItem.product, id=product_id)
#         context = super(CheckTemplate, self).get_context_data(**kwargs)
#         context.update({
#             'product': product,
#             'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
#         })
#         return context


class CreateCheckoutSession(View):
    def post(self, request, *args, **kwargs):
        domain = 'http://localhost:8000/payment'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1NVvOdDploYopxA2zzM4vuo2',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url, code=HTTPStatus.SEE_OTHER)
