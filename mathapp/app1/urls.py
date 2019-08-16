from django.urls import path
from . import views

# import class based views from views.app for post related content on forums
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import FunctionCreateView, FunctionListView, FunctionDetailView, FunctionDeleteView

urlpatterns = [
        path('',views.home,name='app-home'),
        # static math pages
        path('quadinfo/',views.quadratics_info,name='quad_info'),
        path('quadquiz/',views.quadratics_quiz,name='quad_quiz'),
        path('polyquiz/',views.polynomial_functions_quiz,name='poly_quiz'),
        path('polyinfo/',views.polynomial_functions_info,name='poly_info'),
        path('trigproofquiz/',views.trigonometric_proofs_quiz,name='trig_proof_quiz'),
        path('trigproofinfo/',views.trigonometric_proofs_info,name='trig_proof_info'),
        path('logarithmquiz/',views.logarithm_quiz,name='log_quiz'),
        # forum page
        path('forum/',PostListView.as_view(),name='forum'),
        # go to specific posts in the forum
        path('forum/post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
        # go to make new post page
        path('forum/post/new/',PostCreateView.as_view(),name='post-create'),
        # update forum post
        path('forum/post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
        # delete posts
        path('forum/post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
        # calculus tool urls
        path('calculus_tool/',FunctionListView.as_view(),name='calculus_tool'),
        path('calculus_tool/function/',FunctionCreateView.as_view(),name='function-create'),
        path('calculus_tool/<int:pk>/',FunctionDetailView.as_view(),name='function-detail'),
        path('calculus_tool/<int:pk>/delete/',FunctionDeleteView.as_view(),name='function-delete'),
        ]
