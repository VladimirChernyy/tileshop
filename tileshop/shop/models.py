from django.contrib.auth import get_user_model
from django.db import models

from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    images = models.ImageField(upload_to='image/categories/',
                               verbose_name='Фото категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:category', kwargs={'category_slug': self.slug})

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Подкатегория')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    images = models.ImageField(upload_to='image/subcategories/',
                               verbose_name='Фото подкатегории')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='subcategory',
                                 blank=True,
                                 null=True
                                 )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    name = models.CharField(max_length=155,
                            verbose_name='Наименование товара')
    stripe_id = models.CharField()
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата добавления товара')
    images = models.ImageField(upload_to='image/products/',
                               verbose_name='Фото товара')
    create_at = models.DateTimeField(auto_created=True,
                                     verbose_name='Дата поступления')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True,
                                    verbose_name='Товар в наличии')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    stock = models.PositiveIntegerField(default=1, verbose_name='Количество')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL,
                                    blank=True, null=True,
                                    related_name='products',
                                    verbose_name='Подкатегория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product', kwargs={'product_slug': self.slug})

    def get_return_price(self):
        return f'{self.price}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'slug'),)


class Comment(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True,
                                on_delete=models.CASCADE,
                                related_name='comment')
    text = models.TextField(verbose_name='Текст',
                            help_text='Напишите коментарий')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comment',
                               verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True)
