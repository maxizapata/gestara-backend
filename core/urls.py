from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cooperatives/', include('cooperatives.urls')),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),

    #path('reservations/', include('reservations.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
