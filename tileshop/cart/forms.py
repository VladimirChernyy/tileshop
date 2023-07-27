from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=10,
                                  label='Кол')
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)
