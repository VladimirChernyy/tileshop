from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>', views.category_list, name='category_list'),
    path('rewies/', views.rewies, name='rewies'),
]