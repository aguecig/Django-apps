from django.urls import path
from . import views

urlpatterns = [
        path('linear_systems/',views.matrix_solutions,name='matrix-solutions'),
        ]