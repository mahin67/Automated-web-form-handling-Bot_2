from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('', home)
    ] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
