from django import forms

class QuadraticForm(forms.Form):
    a = forms.DecimalField(label='a')
    b = forms.DecimalField(label='b')
    c = forms.DecimalField(label='c')