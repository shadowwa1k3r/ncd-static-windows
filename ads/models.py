from django.db import models


class AdsBlock(models.Model):
    name = models.TextField(default='', blank=True)
    size = models.IntegerField(default=2, blank=True)


class AdsBlockImage(models.Model):
    image = models.FileField(upload_to='cms/ads/', blank=True)
    block = models.ForeignKey(AdsBlock, on_delete=models.CASCADE, blank=True)
