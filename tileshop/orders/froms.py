from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    model = Order
    fields = ['first_name', 'last_name', 'email', 'address', 'city']
