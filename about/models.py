from django.db import models


class About(models.Model):
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField()

    class Meta:
        db_table = 'about'

    def __init__(self):
        return self.title
