from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline

from places.models import Place, PlaceImage


class InlineImage(SortableStackedInline):
    model = PlaceImage
    extra = 1
    readonly_fields = ['image_preview', 'original_size', 'preview_size']

    def original_size(self, obj):
        width = obj.image.width
        height = obj.image.height
        return f'''width: {width}
         height:{height}'''

    def preview_size(self, obj):
        cap = 200
        width = obj.image.width
        height = obj.image.height
        if width > height:
            height = (height/ width) * cap
            width = cap

        elif width < height:
            width = (width / height) * cap
            height = cap
        else:
            width = 200
            height = 200

        return f'''width: {width}
         height:{height}'''

    def image_preview(self, obj):
        cap = 200
        width = obj.image.width
        height = obj.image.height
        if width > height:
            height = (height/ width) * cap
            width = cap

        elif width < height:
            width = (width / height) * cap
            height = cap
        else:
            width = 200
            height = 200
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=width,
            height=height,
        ))


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
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


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):

    fields = ['place', 'image', 'image_preview', ]
    readonly_fields = ['image_preview', ]
    list_display = ['image_preview', 'my_order', 'id', 'place', 'my_order']
    list_filter = ['place__title',]
    search_fields = ['id',]
    search_help_text = 'Please use image id for search. You can also use filter by place.'

    def image_preview(self, obj):
        cap = 200
        width = obj.image.width
        height = obj.image.height
        if width > height:
            height = (height/ width) * cap
            width = cap

        elif width < height:
            width = (width / height) * cap
            height = cap
        else:
            width = 200
            height = 200
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=width,
            height=height,
        ))

