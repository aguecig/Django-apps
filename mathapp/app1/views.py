from django.shortcuts import render,redirect
from django.http import HttpResponse


# dummy data

def home(request):
    return render(request,'app1/home.html')

def quadratics_quiz(request):
    return render(request,'app1/quadratics_quiz.html')


def test(request):
    alpha_dict= {'a': '1', 'b': '2'}
    word = 'Test-word'
    x = [str(i) for i in range(10)]
    context= {
        'alpha_dict': alpha_dict,
        'word': word,
        'x':x
        }
    return render(request,'app1/test.html',context)