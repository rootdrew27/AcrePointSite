from django.db import models
from django.core.files.images import ImageFile
from PIL import Image
from io import BytesIO
from django.core.files import File


def compress_image(image:models.FileField):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img_ouput = BytesIO()
    img.save(img_ouput, 'JPEG', quality=80)
    compressed_image = File(img_ouput, name=image.name)
    return compressed_image

# Create your models here.
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
        
    def save(self, *args, **kwargs):
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def resize_image(self):
        img = Image.open(self.image, 'r')
        img.load()
        img.resize((300, 300))
        return img

    def __str__(self):
        return self.description
        
    
