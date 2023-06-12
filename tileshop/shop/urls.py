from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('category_products/<slug:slug>', views.category_products, name='category_products'),
    path('rewies/', views.rewies, name='rewies'),
]