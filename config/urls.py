from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marketplace.products.urls', namespace='products')),
    path('accounts/', include('marketplace.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include('marketplace.products.urls', namespace='products-api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
