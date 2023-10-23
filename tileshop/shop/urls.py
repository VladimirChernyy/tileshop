from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('category/<slug:category_slug>',
         views.category_list, name='category'),
    path('products/<slug:product_slug>/',
         views.product_detail, name='product'),
    path('create_review/<int:product_id>',
         views.create_review, name='create_review'),
    path('', views.index, name='index'),
]
