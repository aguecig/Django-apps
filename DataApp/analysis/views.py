from django.shortcuts import render, redirect
from .models import Function
from .forms import MatrixForm
from django.views.generic import CreateView, ListView, DetailView, DeleteView

def home(request):
    pass

def get_matrix(request):
    if request.method == 'POST':
        form = MatrixForm(request.POST)
        if form.is_valid():
            a1 = form.cleaned_data['a1']
            a2 = form.cleaned_data['a2']
            b1 = form.cleaned_data['b1']
            b2 = form.cleaned_data['b2']
            d1 = form.cleaned_data['d1']
            d2 = form.cleaned_data['d2']
            F = {'a1':a1,
                 'a2':a2,
                 'b1':b1,
                 'b2':b2,
                 'd1':d1,
                 'd2':d2}
            return render(request,'analysis/database.html',F)
    else:
        form = MatrixForm()
        
    return render(request,'analysis/matrix.html', {'form':form})


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
    fields = ['title','func','limit_point']             # ie analysis/function_form.html

    def form_valid(self,form):
        return super().form_valid(form)
    
class FunctionDetailView(DetailView):
    model = Function
    
class FunctionDeleteView(DeleteView):
    model = Function
    success_url = '/database'
    
