from django.urls import path
from . import views

urlpatterns = [
        path('model_images/',views.model_images,name='model-images'),
        ]