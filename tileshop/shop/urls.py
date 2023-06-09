from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoty/', views.category, name='category'),
    path('rewies/', views.rewies, name='rewies'),
]