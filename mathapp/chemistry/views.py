from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import OrgoChemForm


class OrgoChemView(TemplateView):
    template_name = 'chemistry/organic_chemistry.html'
    
    def get(self,request):
        form = OrgoChemForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        if request.method == 'POST':
            form = OrgoChemForm(request.POST)
            if form.is_valid():
                q1 = form.cleaned_data['q1']
                q2 = form.cleaned_data['q2']
                q3 = form.cleaned_data['q3']
                q4 = form.cleaned_data['q4']
                q5 = form.cleaned_data['q5']
                q6 = form.cleaned_data['q6']
                q7 = form.cleaned_data['q7']
                q8 = form.cleaned_data['q8']
                q9 = form.cleaned_data['q9']
                q10 = form.cleaned_data['q10']
                F = {'form':form,
                     'q1':q1,
                     'q2':q2,
                     'q3':q3,
                     'q4':q4,
                     'q5':q5,
                     'q6':q6,
                     'q7':q7,
                     'q8':q8,
                     'q9':q9,
                     'q10':q10,}
                return render(request,self.template_name,F)