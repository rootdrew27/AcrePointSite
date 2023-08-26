from django.urls import path
from Gallery import views

urlpatterns = [
    path('', views.GalleryIndex, name='GalleryIndex'),
    path('detail/<int:pk>/', views.GalleryDetail, name='GalleryDetail'),
]
