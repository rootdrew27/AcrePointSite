from django.contrib import admin
from Gallery.models import GalleryCategory, GalleryItem


class GalleryCategoryAdmin(admin.ModelAdmin):
    pass

class GalleryItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)
