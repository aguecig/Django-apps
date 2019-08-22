from django.urls import path
from . import views
import sys
sys.path.append("..")
from calctool.views import FunctionListView, FunctionCreateView, FunctionDeleteView, FunctionDetailView
from matrixtool.views import MatrixView
# import class based views from views.app for post related content on forums
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
        path('',views.home,name='app-home'),
        # Quizzes and info sheet urls
        path('quadinfo/',views.quadratics_info,name='quad_info'),
        path('quadquiz/',views.quadratics_quiz,name='quad_quiz'),
        path('polyquiz/',views.polynomial_functions_quiz,name='poly_quiz'),
        path('polyinfo/',views.polynomial_functions_info,name='poly_info'),
        path('trigproofquiz/',views.trigonometric_proofs_quiz,name='trig_proof_quiz'),
        path('trigproofinfo/',views.trigonometric_proofs_info,name='trig_proof_info'),
        path('logarithmquiz/',views.logarithm_quiz,name='log_quiz'),
        path('logarithminfo/',views.logarithm_info,name='log_info'),
        path('rationalquiz/',views.rational_functions_quiz,name='rational_quiz'),
        path('rationalinfo/',views.rational_functions_info,name='rational_info'),
        path('trig12quiz/',views.trig12_quiz,name='trig12_quiz'),
        # forum urls
        path('forum/',PostListView.as_view(),name='forum'),
        path('forum/post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
        path('forum/post/new/',PostCreateView.as_view(),name='post-create'),
        path('forum/post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
        path('forum/post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
        # calculus tool urls
        path('calculus_tool/',FunctionListView.as_view(),name='calculus_tool'),
        path('calculus_tool/function/',FunctionCreateView.as_view(),name='function-create'),
        path('calculus_tool/<int:pk>/',FunctionDetailView.as_view(),name='function-detail'),
        path('calculus_tool/<int:pk>/delete/',FunctionDeleteView.as_view(),name='function-delete'),
        # matrix tool urls
        path('linear_systems/',MatrixView.as_view(),name='matrix-solutions'),
        ]