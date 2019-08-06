from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('stock/', include('stock.urls')),
    path('purchases/', include('purchases.urls')),
    # path('suppliers/', include('suppliers.urls')),
    path('', RedirectView.as_view(pattern_name='users:new', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
