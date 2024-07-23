from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    country = models.CharField(max_length=10, default='kr')
    upload_date = models.DateTimeField(auto_now_add=True)
    video_url = models.CharField(max_length=255)
    thumbnail_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
