from django import forms

class MatrixForm(forms.Form):
    a1 = forms.DecimalField(label='a1')
    b1 = forms.DecimalField(label='b1')
    d1 = forms.DecimalField(label='d1')
    a2 = forms.DecimalField(label='a2')
    b2 = forms.DecimalField(label='b2')
    d2 = forms.DecimalField(label='d2')