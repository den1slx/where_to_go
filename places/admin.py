from django.contrib import admin

from places.models import Place, PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            'Place',
            {
                'fields': ['title', 'description_short', 'description_long'],
            },
        ),
        (
            'Coordinates',
            {
                'fields': ['lng', 'lat']
            }
        )
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    fields = ['place', 'image']
    search_fields = ['place__id',]




