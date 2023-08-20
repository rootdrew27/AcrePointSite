from django.contrib import admin
from Gallery.models import GalleryCategory, GalleryItem
# Register your models here.

class GalleryCategoryAdmin(admin.ModelAdmin):
    pass

class GalleryItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)
