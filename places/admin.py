from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline

from places.models import Place, PlaceImage


class InlineImage(SortableStackedInline):
    model = PlaceImage
    extra = 1

    def original_size(self, obj):
        width = obj.image.width
        height = obj.image.height
        return f'''width: {width}
         height:{height}'''

    def image_preview(self, obj):
        if obj.image.width > obj.image.height:
            width = 200
            height = 'auto'
        elif obj.image.height > obj.image.width:
            width = 'auto'
            height = 200
        else:
            width = 200
            height = 200
        return format_html('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=obj.image.url,
            width=width,
            height=height,
        ))

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['image_preview', 'original_size', ]
        else:
            return []


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ['title',]
    inlines = [InlineImage, ]
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
    ]
