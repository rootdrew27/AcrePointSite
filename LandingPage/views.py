from django.shortcuts import render
from Gallery.models import GalleryItem


def LandingPageIndex(request):
    gallery_items = GalleryItem.objects.all()[:6]
    
    gallery_item_with_categories = []

    for gallery_item in gallery_items:
        gallery_categories = ",".join([category.title for category in gallery_item.categories.all()])
        gallery_item_with_categories.append((gallery_item, gallery_categories))

    context = {
        'gallery_items_with_categories': gallery_item_with_categories
    }
    return render(request, 'LandingPage/index.html', context)

