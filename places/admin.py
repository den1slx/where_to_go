from django.contrib import admin

from places.models import Place, PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ['title', 'description_short', 'description_long', 'lng', 'lat', 'imgs']


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    fields = ['place', 'image']
    search_fields = ['place__id',]




