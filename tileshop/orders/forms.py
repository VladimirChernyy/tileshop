from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'city',
        )

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget = forms.TextInput(attrs={'class': 'form-control'})
