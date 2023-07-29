from django.shortcuts import render
from Gallery.models import *

# Create your views here.
def GalleryIndex(request):
    categories = Category.objects.all()
    image_cards = ImageCard.objects.all()

    context = {
        'categories': categories,
        'image_cards': image_cards,
    }
    return render(request, "Gallery/index.html", context)

def GalleryDetail(request, pk):
    image_card = ImageCard.objects.get(pk=pk)
    context = {
        'image_card': image_card,
    }
    return render(request, 'Gallery/detail.html', context)

def GalleryFilter(request, Categories:list):
  
    image_cards = Category.objects.none() #Try these instead: django.db.models.query.EmptyQuerySet OR django.db.models.query.QuerySet
    for category in Categories:
        image_cards = image_cards | ImageCard.objects.filter(category=category)
    
    context = {
        'image_cards': image_cards,
    }
    return render(request, "Gallery/_images.html", context)


