from django.db import models


class BaseData(models.Model):
    waterMark = models.ImageField(upload_to='storage/waterMarks/', null=True, blank=True)
    video = models.FileField(upload_to='storage/videos/', null=True, blank=True)
    baseDataId = models.CharField(max_length=255)


class ConvertedVideos(models.Model):
    convertedVideo = models.FileField(upload_to='storage/convertedVideos/', null=True, blank=True)
    convertedVideoId = models.CharField(max_length=255)