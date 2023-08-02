from django.shortcuts import render
from Gallery.models import Category, ImageCard

# Create your views here.
def GalleryIndex(request):
    try: 
        categories = Category.objects.all()
        image_cards = ImageCard.objects.all()

        for image_card in image_cards:
            image_card.image = image_card.compress_image()
            
    except FileNotFoundError as ex:
        #Log 
        pass
    
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


