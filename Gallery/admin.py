from django.contrib import admin
from Gallery.models import StyleCategory, ImageCard
# Register your models here.

class StyleCategoryAdmin(admin.ModelAdmin):
    pass

class ImageCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(StyleCategory, StyleCategoryAdmin)
admin.site.register(ImageCard, ImageCardAdmin)
