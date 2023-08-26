from django.shortcuts import render
from Services.models import Service, ServiceImage


def ServicesIndex(request):

    services = Service.objects.all()

    services_and_primary_images = [] # list of tuples : (service, primary_image)

    for service in services:
        for service_image in service.service_image.all():
            if service_image.classification == "primary":
                services_and_primary_images.append(service, service_image)

    context = {
        'services_and_primary_images': services_and_primary_images 
    }

    return render(request, "Services/index.html", context)