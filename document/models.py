from django.db import models


class Document(models.Model):
    name_uz = models.TextField(blank=True, default='')
    name_ru = models.TextField(blank=True, default='')
    name_en = models.TextField(blank=True, default='')
    file = models.FileField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'cms_faq'
        ordered = '-id'

    def __str__(self):
        return self.name_ru or self.name_en or self.name_uz or 'asd'
