from django.shortcuts import render
from Gallery.models import GalleryCategory, GalleryItem

# Create your views here.
def GalleryIndex(request):
    categories = GalleryCategory.objects.all()
    items = GalleryItem.objects.all()

    items_with_categories = []

    for item in items:
        item_categories = ",".join([category.title for category in item.categories.all()])
        items_with_categories.append((item, item_categories))

    context = {
        'categories': categories,
        'items_with_categories': items_with_categories
    }
    return render(request, "Gallery/index.html", context)

def GalleryDetail(request, pk):
    item = GalleryItem.objects.get(pk=pk)
    context = {
        'item': item,
    }
    return render(request, 'Gallery/detail.html', context)


