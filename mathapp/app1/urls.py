from django.urls import path
from . import views

# import class based views from views.app for post related content on forums
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
        path('',views.home,name='app-home'),
        # static math pages
        path('quadinfo/',views.quadratics_info,name='quad_info'),
        path('quadquiz/',views.quadratics_quiz,name='quad_quiz'),
        path('polyquiz/',views.polynomial_functions_quiz,name='poly_quiz'),
        path('polyinfo/',views.polynomial_functions_info,name='poly_info'),
        path('trigproofquiz/',views.trigonometric_proofs_quiz,name='trig_proof_quiz'),
        path('trigproofinfo/',views.trigonometric_proofs_info,name='trig_proof_info'),
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
        ]