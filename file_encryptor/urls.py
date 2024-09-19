from django.urls import path
from .views import health_check,upload_and_encrypt_file

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('upload/', upload_and_encrypt_file, name='upload_and_encrypt'),
]
