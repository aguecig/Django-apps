from django.shortcuts import render, redirect
from .models import Function
from django.views.generic import CreateView, ListView, DetailView, DeleteView

def home(request):
    pass

def database(request):
    
    context = {
        'functions':Function.objects.all()
        }

    return render(request,'analysis/database.html',context)

class FunctionListView(ListView):
    model = Function
    # change template
    template_name = 'analysis/database.html' 
    context_object_name = 'functions'        

class FunctionCreateView(CreateView):
    model = Function                      # <app>/<model>_<viewtype>.html path
    fields = ['title','func']             # ie analysis/function_form.html

    def form_valid(self,form):
        return super().form_valid(form)
    
class FunctionDetailView(DetailView):
    model = Function
    
class FunctionDeleteView(DeleteView):
    model = Function
    success_url = '/database'