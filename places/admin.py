from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline

from django.contrib import admin
from django.utils.html import format_html

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
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px;"/>',
            obj.image.url,
        )

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


@admin.register(PlaceImage)
class ImageeAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['id', ]
    search_help_text = 'Поиск по id картинки'
    list_filter = ['place__title',]
    readonly_fields = ['image_preview',]
    list_display = ['image_preview', 'id', 'ordering',]
    ordering = ['ordering',]

    def image_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px;"/>',
            obj.image.url,
        )
