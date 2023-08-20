from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Place(models.Model):
    title = models.CharField('Название', max_length=200, null=True)
    description_short = models.CharField('краткое описание', null=True, max_length=350)
    lng = models.FloatField('longitude', null=True)
    lat = models.FloatField('latitude', null=True)
    description_long = HTMLField('Описание', null=True, blank=True)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(upload_to='images/')
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE, related_name='images')
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        editable=True,
        unique=False,
    )

    def __str__(self):
        return f'{self.place.title} image{self.place.id}{self.id}'

    class Meta:
        ordering = ['my_order',]
        verbose_name_plural = "Images"



