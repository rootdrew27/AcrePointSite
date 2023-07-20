from django.shortcuts import render
from Gallery.models import *



# Create your views here.
def GalleryIndex(request):
    styles = StyleCategory.objects.all()

    context = {

        'styles': styles
    }
    return render(request, "index.html", context)


def GalleryFilter(request, *styleCategory):
  
    images = StyleCategory.objects.none() #Try these instead: django.db.models.query.EmptyQuerySet OR django.db.models.query.QuerySet
    for style in styleCategory:
        images = images | ImageCard.objects.filter(description=style)

    context = {
        'images': images
    }
    return render(request, "_images.html", context)


