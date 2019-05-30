from django.db import models


class About(models.Model):
    title_uz = models.TextField()
    title_ru = models.TextField()
    title_en = models.TextField()
    content_uz = models.TextField()
    content_ru = models.TextField()
    content_en = models.TextField()
    image = models.ImageField()
    status = models.BooleanField()

    class Meta:
        db_table = 'cms_about'

    def __init__(self):
        return self.title_ru or self.title_en or self.title_uz or 'asd'
