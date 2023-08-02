from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    city = models.CharField(max_length=180, verbose_name='Город')
    phone_number = PhoneNumberField(region='RU', verbose_name='Номер телефона',
                                    help_text='+7 (___) ___ - __ - __')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Заказ создан')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Заказ обновлен')
    paid = models.BooleanField(default=False, verbose_name='Оплата')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Заказ {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity


