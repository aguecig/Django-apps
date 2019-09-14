from django.urls import path
from . import views

urlpatterns = [
        path('organic_chemistry/',views.organic_chemistry,name='organic-chemistry'),
        ]