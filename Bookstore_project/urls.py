from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', include('cart.urls', namespace='cart')),
    path('accounts/', include('allauth.urls')),
    path('discount/', include('discount.urls', namespace='discount')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('callback/', include('callback.urls', namespace='callback')),
    path('', include('bookstore_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)