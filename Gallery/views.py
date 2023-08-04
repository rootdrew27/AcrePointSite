from django.shortcuts import render
from Gallery.models import *

# Create your views here.
def GalleryIndex(request):
    categories = Category.objects.all()
    image_cards = list(ImageCard.objects.all())

    image_cards_with_categories = []

    for image_card in image_cards:
        img_card_categories = list(image_card.categories.all())
        categories_titles = [] 
        for category in img_card_categories:
            categories_titles.append(category.title)
        image_cards_with_categories.append((image_card, ','.join(categories_titles)))

    page_title = "Our Projects"

    context = {
        'page_title': page_title,
        'categories': categories,
        'image_cards_with_categories': image_cards_with_categories
    }
    return render(request, "Gallery/index.html", context)

def GalleryDetail(request, pk):
    image_card = ImageCard.objects.get(pk=pk)
    context = {
        'image_card': image_card,
    }
    return render(request, 'Gallery/detail.html', context)


# def GalleryFilter(request, Categories:list):
  
#     image_cards = Category.objects.none() #Try these instead: django.db.models.query.EmptyQuerySet OR django.db.models.query.QuerySet
#     for category in Categories:
#         image_cards = image_cards | ImageCard.objects.filter(category=category)
    
#     context = {
#         'image_cards': image_cards,
#     }
#     return render(request, "Gallery/_images.html", context)


