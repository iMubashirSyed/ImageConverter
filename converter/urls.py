from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download_image', views.download_image, name='download_image'),
]