from django import forms

from tileshop.constans import CartLimit, CartValidate


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        initial=CartLimit.QUANTITY_INITIAL.value,
        min_value=CartValidate.QUANTITY_MIN_VALUE.value,
        max_value=CartValidate.QUANTITY_MAX_VALUE.value,
        label='Кол'
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
