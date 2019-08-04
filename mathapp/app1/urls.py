from django.urls import path
from . import views

# import class based views from views.app
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
        path('',views.home,name='app-home'),
        path('quadinfo/',views.quadratics_info,name='quad_info'),
        path('quadquiz/',views.quadratics_quiz,name='quad_quiz'),
        path('forum/',PostListView.as_view(),name='forum'),
        # go to specific posts in the forum
        path('forum/post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
        # go to new post page
        path('forum/post/new/',PostCreateView.as_view(),name='post-create'),
        # update forum posts
        path('forum/post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
        # delete posts
        path('forum/post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
        ]