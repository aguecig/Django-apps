from django.shortcuts import render,redirect
from django.http import HttpResponse

# we can set post formats in the models directory
from .models import Function

# import post views
from django.views.generic import ListView, DetailView, CreateView, DeleteView

def calculus_tool(request):
    
    context = {
        'equations':Function.objects.all()
        }

    return render(request,'app1/calculus_tool.html',context)

class FunctionListView(ListView):
    model = Function
    # change template
    template_name = 'calctool/calculus_tool.html' 
    context_object_name = 'equations'        

class FunctionCreateView(CreateView):
    model = Function                      # <app>/<model>_<viewtype>.html path
    fields = ['equation']             # ie analysis/function_form.html

    def form_valid(self,form):
        return super().form_valid(form)
    
class FunctionDetailView(DetailView):
    model = Function
    
class FunctionDeleteView(DeleteView):
    model = Function
    success_url = '/calculus_tool'