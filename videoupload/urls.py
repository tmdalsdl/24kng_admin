from django.urls import path
from .views import admin_page, video_upload

urlpatterns = [
    path('adminpage/', admin_page, name='admin_page'),
    path('upload/', video_upload, name='video_upload'),
]
