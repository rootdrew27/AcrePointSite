from django.contrib import admin
from Services.models import Service, ServiceImage, ServiceImageType

class ServiceAdmin(admin.ModelAdmin):
    pass

class ServiceImageAdmin(admin.ModelAdmin):
    pass

class ServiceImageTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImage, ServiceImageAdmin)
admin.site.register(ServiceImageType, ServiceImageTypeAdmin)
