from django.contrib import admin
from django.urls import path, include 
from LandingPage import views

urlpatterns = [
    path('', views.LandingPageIndex, name='LandingPageIndex'),
]
