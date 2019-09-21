from django.urls import path
from . import views
import sys
sys.path.append("..")
from calctool.views import FunctionListView, FunctionCreateView, FunctionDeleteView, FunctionDetailView
from matrixtool.views import MatrixView
from quadratictool.views import QuadraticView
from modelling3D.views import Model3dView
from chemistry.views import OrgoChemView
# import class based views from views.app for post related content on forums
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
        path('',views.home,name='app-home'),
        # Quizzes and info sheet high school urls
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
        path('trig12info/',views.trig12_info,name='trig12_info'),
        path('relfuncquiz/',views.relations_functions_quiz,name='relations_functions_quiz'),
        path('relfuncinfo/',views.relations_functions_info,name='relations_functions_info'),
        path('limitsquiz/',views.limits_quiz,name='limits_quiz'),
        path('limitsinfo/',views.limits_info,name='limits_info'),
        path('derivquiz/',views.deriv_quiz,name='deriv_quiz'),
        path('derivinfo/',views.deriv_info,name='deriv_info'),
        path('optquiz/',views.opt_quiz,name='opt_quiz'),
        path('optinfo/',views.opt_info,name='opt_info'),
        path('permutationquiz/',views.permutation_quiz,name='permutation_quiz'),
        path('permutationinfo/',views.permutation_info,name='permutation_info'),
        path('combinationquiz/',views.combination_quiz,name='combination_quiz'),
        path('rationalexpressionsquiz/',views.rational_expressions_quiz,name='rational_express_quiz'),
        # forum urls
        path('forum/',PostListView.as_view(),name='forum'),
        path('forum/post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
        path('forum/post/new/',PostCreateView.as_view(),name='post-create'),
        path('forum/post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
        path('forum/post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
        # advanced topics urls
        path('graph_theory_notes/',views.graph_theory_notes,name='graph-theory-notes'),
        path('abstract_algebra_notes/',views.abstract_algebra_notes,name='abstract-algebra-notes'),
        path('calc_manifolds_notes/',views.calc_manifolds_notes,name='calc-manifolds-notes'),
        path('calc_manifolds_problems/',views.calc_manifolds_problems,name='calc-manifolds-problems'),
        path('prob_stats_notes/',views.prob_stats_notes,name='prob-stats-notes'),
        # calculus tool urls
        path('calculus_tool/',FunctionListView.as_view(),name='calculus_tool'),
        path('calculus_tool/function/',FunctionCreateView.as_view(),name='function-create'),
        path('calculus_tool/<int:pk>/',FunctionDetailView.as_view(),name='function-detail'),
        path('calculus_tool/<int:pk>/delete/',FunctionDeleteView.as_view(),name='function-delete'),
        # matrix tool urls
        path('linear_systems/',MatrixView.as_view(),name='matrix-solutions'),
        # quadratic tool urls
        path('quadratic_analysis/',QuadraticView.as_view(),name='quad-analysis'),
        # 3d model urls
        path('model_images/',Model3dView.as_view(),name='model-images'),
        # chemistry urls
        path('organic_chemistry/',OrgoChemView.as_view(),name='organic-chemistry'),
        ]