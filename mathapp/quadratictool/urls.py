from django.urls import path
from . import views

urlpatterns = [
        path('quadratic_analysis/',views.quadratic_tool,name='quad-analysis'),
        ]