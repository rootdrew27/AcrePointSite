from django.urls import path 
from Services import views

urlpatterns = [
    path('', views.ServicesIndex, name="ServicesIndex"),
    # path('detail/<int:pk>/', views.ServicesDetail, name="ServicesDetail")
]
