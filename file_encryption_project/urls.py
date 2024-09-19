from django.contrib import admin
from django.urls import path, include
from file_encryptor.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('file_encryptor.urls')),
    path('', health_check, name='health_check'),
]
