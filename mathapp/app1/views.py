from django.shortcuts import render,redirect
from django.http import HttpResponse

# we can set post formats in the models directory
from .models import Post, Function

# import post views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# import required login to make post, as well as update there own posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 



# create function based views for webpages on the site

def home(request):
    return render(request,'app1/home.html')

def quadratics_quiz(request):
    return render(request,'app1/quadratics_quiz.html')

def quadratics_info(request):
    return render(request,'app1/quadratics_info.html')

def polynomial_functions_quiz(request):
    return render(request,'app1/polynomial_functions_quiz.html')

def polynomial_functions_info(request):
    return render(request,'app1/polynomial_functions_info.html')

def trigonometric_proofs_quiz(request):
    return render(request,'app1/trigonometric_proofs_quiz.html')

def trigonometric_proofs_info(request):
    return render(request,'app1/trigonometric_proofs_info.html')

def logarithm_quiz(request):
    return render(request,'app1/logarithm_quiz.html')

def forum(request):  
    context = {
                'posts':Post.objects.all()
                }
    return render(request,'app1/forum.html',context)


# create class based views for making posts, updating
# posts, deleting posts on the site forum
    
class PostListView(ListView):
    model = Post
    # change template
    template_name = 'app1/forum.html'
    context_object_name = 'posts'
    # display newest posts first
    ordering = ['-date_posted']
    # set max posts per page
    paginate_by = 5
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # only update posts that you are author of
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False  # will return 403 Forbidden
        
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    
    # can only delete your own posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False  # will return 403 Forbidden
    
    # return to forums upon deleting post
    success_url = '/forum'
    
def calculus_tool(request):
    
    context = {
        'functions':Function.objects.all()
        }

    return render(request,'app1/calculus_tool.html',context)

class FunctionListView(ListView):
    model = Function
    # change template
    template_name = 'app1/calculus_tool.html' 
    context_object_name = 'functions'        

class FunctionCreateView(CreateView):
    model = Function                      # <app>/<model>_<viewtype>.html path
    fields = ['function']             # ie analysis/function_form.html

    def form_valid(self,form):
        return super().form_valid(form)
    
class FunctionDetailView(DetailView):
    model = Function
    
class FunctionDeleteView(DeleteView):
    model = Function
    success_url = '/calculus_tool'