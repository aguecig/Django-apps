from django.shortcuts import render,redirect

# import user forms stuff
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm 

# profile restriction import
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # saves the user, can check under admin page
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('app-home')
            
    else:
        form = UserRegisterForm()
        return render(request,'users/register.html',{'form':form})
    
@login_required       # login decorator, will redirect to login route if not logged in
def profile(request):
    return render(request,'users/profile.html')