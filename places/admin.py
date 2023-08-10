from django.contrib import admin

from places.models import Place



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ['title', 'description_short', 'description_long', 'lng', 'lat', 'imgs']



