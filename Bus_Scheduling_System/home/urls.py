from django.contrib import admin
from django.urls import path

urlpatterns = [ 
    path('admin', admin.site.urls),
     path('', include('home.urls')),
]

from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)