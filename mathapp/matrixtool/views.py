from django.shortcuts import render
from .forms import MatrixForm
from django.views.generic import TemplateView

class MatrixView(TemplateView):
    
    template_name = 'matrixtool/matrix_solutions.html'

    def get(self,request):
        form = MatrixForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        if request.method == 'POST':
            form = MatrixForm(request.POST)
            if form.is_valid():
                a1 = form.cleaned_data['a1']
                a2 = form.cleaned_data['a2']
                b1 = form.cleaned_data['b1']
                b2 = form.cleaned_data['b2']
                d1 = form.cleaned_data['d1']
                d2 = form.cleaned_data['d2']
                F = {'form':form,
                     'a1':a1,
                     'a2':a2,
                     'b1':b1,
                     'b2':b2,
                     'd1':d1,
                     'd2':d2}
                return render(request,self.template_name,F)