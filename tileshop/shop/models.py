from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=155,
                            verbose_name='Наименование товара')
    description = models.TextField(verbose_name='Описание')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата добавления товара')
    create_at = models.DateTimeField(auto_created=True,
                                     verbose_name='Дата поступления')
    product_stock = models.BooleanField(default=True,
                                        verbose_name='Товар в наличии')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Rewies(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='rewies',
                               verbose_name='Автор отзыва')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='rewies',
                                verbose_name='Товар')
    description = models.TextField(verbose_name='Описание',
                                   help_text='Напишите отзыв')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.author, self.description

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
