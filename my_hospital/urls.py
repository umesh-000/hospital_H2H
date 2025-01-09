from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [

    path('', include('accounts.urls')),

     path('dj/', admin.site.urls),
    
    path('admin/', include('H2H_admin.urls')),

    path('auth/', include('rest_framework_social_oauth2.urls')),
    
    # Bed Booking API's
    path('api/', include('H2H_admin.urls_api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)