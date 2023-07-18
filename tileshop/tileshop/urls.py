from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'auth/', include('django.contrib.auth.urls')),
    path(r'cart/', include('cart.urls', namespace='cart')),
    path(r'orders/', include('orders.urls', namespace='orders')),
    path(r'', include('shop.urls', namespace='shop')),
    # path('auth/', include('users.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
