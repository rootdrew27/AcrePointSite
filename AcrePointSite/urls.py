from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LandingPage.urls')),
    path('Gallery/', include('Gallery.urls')),
    path('Services/', include('Services.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The following code can be used to serve MEDIA files from a disk (for use in deploying)

# from django.views.static import serve
# from django.urls import re_path

# urlpatterns += [
#     re_path(r'^media/(?P<path>.*)$', serve, {
#         'document_root': settings.MEDIA_ROOT,
#     }),
# ]