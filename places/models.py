from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', default='')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')
    description_long = HTMLField('Описание', default='', blank=True)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField('Картинка', upload_to='images/')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    ordering = models.PositiveIntegerField(
        default=0,
        db_index=True,
        editable=True,
        blank=True,
        verbose_name='Упорядочение'
    )

    def __str__(self):
        return f'{self.place.title} image{self.place.id}{self.id}'

    class Meta:
        ordering = ['ordering',]
        verbose_name_plural = "Images"



