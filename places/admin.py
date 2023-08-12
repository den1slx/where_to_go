from django.contrib import admin

from places.models import Place, PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ['path',]
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
        ),
        (
            'Path to json',
            {
                'fields': ['path',]
            }
        )
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    fields = ['place', 'image']
    search_fields = ['id',]
    list_filter = ['place__id',]




