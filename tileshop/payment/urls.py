from django.urls import path

from payment.views import (CreateCheckoutSession,
                           # CheckTemplate,
                           SuccessView,
                           CancelView)

app_name = 'payment'

urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    # path('', CheckTemplate.as_view(), name='check'),
    path('create-checkout-session/', CreateCheckoutSession.as_view(),
         name='create-checkout-session'),

]
