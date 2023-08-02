from django.db import models
from django.core.files.images import ImageFile
from PIL import Image
from io import BytesIO
from django.core.files import File 
from pathlib import Path


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ImageCard(models.Model):
    description = models.CharField(null=True, blank=True, max_length=200)
    image = models.ImageField(upload_to="Gallery/", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('Category', related_name='image_cards', default='NA')

    
    #ToDo: order by 'most clicks' or by Diegos preference
    class Meta:
        ordering = ["-date_created"]
        
    # def save(self, *args, **kwargs):
    #     self.image = compress_image(self.image)
    #     super(ImageCard, self).save(*args, **kwargs)


    def compress_image(self):
        try:  
            img = Image.open(self.image)
            if img.mode != "RGB":
                img = img.convert("RGB")
            img_ouput = BytesIO()
            img.save(img_ouput, 'JPEG', quality=1)
            compressed_image = File(img_ouput, name=self.image.name)
            return compressed_image
        except FileNotFoundError as ex:
            raise FileNotFoundError 

    def resize_image(self):
        img = Image.open(self.image, 'r')
        img.load()
        img.resize((300, 300))
        return img

    def __str__(self):
        return self.description
        
    
