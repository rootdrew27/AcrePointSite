from django.db import models

# Create your models here.
class StyleCategory(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class ImageCard(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(width_field=480, height_field=480)
    date_created = models.DateTimeField(auto_now_add=True)
    style = models.ManyToManyField('StyleCategory', related_name='image_cards', default='NA')

    #ToDo: order by 'most clicks' or by Diegos preference
    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.description
        

