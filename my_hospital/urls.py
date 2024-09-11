from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    path('api/', include('hospital.urls_api')),

    # Hospital Panel
    path('hospital_panel/', include('hospital_panel.urls')),

    # Doctor
    path('admin/', include('doctor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)