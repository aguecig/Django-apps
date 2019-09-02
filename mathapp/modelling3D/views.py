from django.shortcuts import render

from django.views.generic import TemplateView

class Model3dView(TemplateView):
    
    template_name = 'modelling3D/model_images.html'