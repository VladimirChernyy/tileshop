from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>',
         views.category_list, name='category'),
    path('products/<slug:product_slug>',
         views.product_detail, name='product'),
    path('reviews/', views.reviews, name='reviews'),
]