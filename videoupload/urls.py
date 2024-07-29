from django.urls import path
from .views import admin_page, video_upload, get_public_ip  # dashboard 삭제

urlpatterns = [
    path('adminpage/', admin_page, name='admin_page'),
    path('upload/', video_upload, name='video_upload'),
    path('get_public_ip/', get_public_ip, name='get_public_ip'),  # 추가된 부분
]
