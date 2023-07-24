from django.contrib import admin
from Gallery.models import Category, ImageCard
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class ImageCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(ImageCard, ImageCardAdmin)
