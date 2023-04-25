from django.db import models

class BaseData(models.Model):
    waterMark = models.ImageField(upload_to='storage/waterMarks/', null=True, blank=True)
    video = models.FileField(upload_to='storage/videos/', null=True, blank=True)