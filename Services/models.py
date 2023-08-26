from django.db import models


class Service(models.Model):
    """
        Service Model
        Contains: title (Charfield), description (Charfield)
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class ServiceImage(models.Model):
    """
        ServiceImage Model
        Contains: title (CharField), classification (ForeignKey), image (ImageField), service (ForeignKey)
    """
    title = models.CharField(max_length=50)
    classification = models.ForeignKey('ServiceImageType', related_name='service_image', null=True, on_delete=models.SET_NULL)  
    service = models.ForeignKey('Service', related_name='service_image', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="Services/", blank=True, null=True, max_length=100)


    def __str__(self):
        return self.title
    

class ServiceImageType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title