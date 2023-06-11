# Generated by Django 4.2 on 2023-06-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_images_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='images',
            field=models.ImageField(upload_to='image/', verbose_name='Фото категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='image/', verbose_name='Фото товара'),
        ),
    ]
