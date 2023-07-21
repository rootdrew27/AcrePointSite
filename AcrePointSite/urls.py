from django.contrib import admin
from django.urls import path, include 
import Gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Gallery.urls'), name="GalleryIndex")
]
