from django.db import models
from django.core.files.images import ImageFile


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ImageCard(models.Model):
    description = models.CharField(null=True, blank=True, max_length=200)
    image = models.FileField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('Category', related_name='image_cards', default='NA')

    #ToDo: order by 'most clicks' or by Diegos preference
    class Meta:
        ordering = ["-date_created"]
        
    def path_to_imgs():
        return "Gallery/images/"

    def __str__(self):
        return self.description
        
    
