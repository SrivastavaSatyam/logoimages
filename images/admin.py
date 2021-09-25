from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Upload




@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    # for i in obj
    def image_tag(self, obj):
        return format_html('<img src="{}"     width=81px;/>'.format(obj.Image_svg.url))
    search_fields = ("name__startswith", )

    image_tag.short_description = 'Image'
    list_display=('image_tag','name','Desc')

    