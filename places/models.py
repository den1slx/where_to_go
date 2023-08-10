from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200, null=True)
    description_short = models.CharField('краткое описание', null=True, max_length=350)
    description_long = models.TextField('Описание', null=True)
    lng = models.FloatField('longitude', null=True)
    lat = models.FloatField('latitude', null=True)
    imgs = models.TextField(null=True)

    def __str__(self):
        return self.title