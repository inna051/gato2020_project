from django.contrib import admin
from django.urls import path, include

from gato2020 import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('main/', include('gato2020.main.urls')),
    path('products/', include('gato2020.products.urls')),
    path('profiles/', include('gato2020.profiles.urls')),
    path('map/', include('gato2020.map.urls')),
    path('clients/', include('gato2020.clients.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)