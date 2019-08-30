from django.shortcuts import render
from .forms import QuadraticForm
from django.views.generic import TemplateView

class QuadraticView(TemplateView):
    
    template_name = 'quadratictool/quadratic_tool.html'
    
    def get(self,request):
        form = QuadraticForm()
        return render(request, self.template_name,{'form':form})
    
    def post(self,request):
        if request.method == 'POST':
            form = QuadraticForm(request.POST)
            if form.is_valid():
                a = form.cleaned_data['a']
                b = form.cleaned_data['b']
                c = form.cleaned_data['c']
                F = {'form':form,
                     'a':a,
                     'b':b,
                     'c':c}
                return render(request,self.template_name,F)