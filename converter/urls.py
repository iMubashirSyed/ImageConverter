from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download/<str:task_id>/', views.download_image, name='download_image'),
    path('progress/<str:task_id>/', views.progress, name='progress'),
] 
