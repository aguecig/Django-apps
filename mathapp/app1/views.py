from django.shortcuts import render,redirect
from django.http import HttpResponse

# we can set post formats in the models directory
from .models import Post

# import post views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# import required login to make post, as well as update there own posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 



# function based views for quizzes and info sheets on high school material

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

def logarithm_info(request):
    return render(request,'app1/logarithm_info.html')

def rational_functions_quiz(request):
    return render(request,'app1/rational_functions_quiz.html')

def rational_functions_info(request):
    return render(request,'app1/rational_functions_info.html')

def trig12_quiz(request):
    return render(request,'app1/trig12_quiz.html')

def trig12_info(request):
    return render(request,'app1/trig12_info.html')

def relations_functions_quiz(request):
    return render(request,'app1/relations_functions_quiz.html')

# functioon based view for the forum

def forum(request):  
    context = {
                'posts':Post.objects.all()
                }
    return render(request,'app1/forum.html',context)

# function based views for advanced topics
    
def graph_theory_notes(request):
    return render(request,'app1/graph_theory_notes.html')

def abstract_algebra_notes(request):
    return render(request,'app1/abstract_algebra_notes.html')
    
def calc_manifolds_notes(request):
    return render(request,'app1/calc_manifolds_notes.html')

def prob_stats_notes(request):
    return render(request,'app1/prob_stats_notes.html')

# create class based views for making posts, updating
# posts, deleting posts on the forum
    
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
    
