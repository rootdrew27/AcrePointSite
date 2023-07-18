from django.shortcuts import render
from Gallery.models import *

# Create your views here.
def GalleryIndex(request):
    images = ImageCard.objects.all()
    styles = StyleCategory.objects.all()
    context = {
        'images': images,
        'styles': styles
    }
    return render(request, "index.html", context)


def GalleryFilter(request, styleCategory):
    images = ImageCard.objects.filter(description=styleCategory)
    context = {
        'images': images
    }
    return (request, "index.html", context)


