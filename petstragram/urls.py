from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstragram.main_app.urls')),
] + static(settings.MEDIA_URL, media_root=settings.MEDIA_ROOT)
